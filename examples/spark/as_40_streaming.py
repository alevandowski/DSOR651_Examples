'''
    This is an example Apache Spark stream processing script. It is based on the
    [guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html).
    The scripts starts up a seperate process that acts as the producer of messages.
'''
import multiprocessing
import time

def simulate_events():
    import socket

    # Define server address and port
    HOST = '0.0.0.0'  # Listen on all interfaces
    PORT = 9999        # Port to listen on

    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    sock.bind((HOST, PORT))

    # Listen for incoming connections
    sock.listen(1)

    print("Server started listening on port", PORT)

    # Accept a connection from a client
    conn, addr = sock.accept()
    print("Connected by", addr)

    for _ in range(10):
        # Prepare the data to send (replace with your actual data)
        # The \n character is important since it indicates to the stream
        # processing that a message is complete.
        data = b"This is some data from the server!\n"

        # Send the data to the client
        conn.sendall(data)
        time.sleep(2)

    # Close the connection
    conn.close()

    # Close the socket
    sock.close()

    print("Server shutting down")

def run_spark_stream_processing():
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import explode
    from pyspark.sql.functions import split

    spark = SparkSession.builder.appName("demo").getOrCreate()

    # Create DataFrame representing the stream of input lines from connection to localhost:9999
    lines = spark \
        .readStream \
        .format("socket") \
        .option("host", "localhost") \
        .option("port", 9999) \
        .load()

    # Split the lines into words
    words = lines.select(
    explode(
        split(lines.value, " ")
    ).alias("word")
    )

    # Generate running word count
    wordCounts = words.groupBy("word").count()
    # Start running the query that prints the running counts to the console
    query = wordCounts \
        .writeStream \
        .outputMode("complete") \
        .format("console") \
        .start()

    query.awaitTermination()


if __name__ == "__main__":
    p = multiprocessing.Process(target=simulate_events)
    p.start()
    time.sleep(2) # waiting a little bit to ensure process's socket server starts
    run_spark_stream_processing()
    p.join()

