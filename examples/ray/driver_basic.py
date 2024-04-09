import ray
import time
import random

# Start Ray. If you're connecting to an existing cluster, you would use
# ray.init(address=<cluster-address>) instead.
ray.init()

# By adding the `@ray.remote` decorator, a regular Python function
# becomes a Ray remote function.
@ray.remote
def my_function(wait_time, msg):
    time.sleep(wait_time)
    print(f"Waited {wait_time} seconds to print out {msg}")
    return 1

# To invoke this remote function, use the `remote` method.
# This will immediately return an object ref (a future) and then create
# a task that will be executed on a worker process.
obj_ref = my_function.remote(random.random(), "Hello World")

# A Ray Worker should now be be processing this in another process.

# A Future object is a reference to an eventual output.

# To wait to get the eventual output, we can do the following with the Future
return_val = ray.get(obj_ref)
print(f"Waited and got the following return value: {return_val}")

# Invocations of Ray remote functions happen in parallel.
# All computations are performed in the background. They are driven by Ray's
# internal schedular which assigns tasks to workers to execute.
obj_refs=[]
for i in range(4):
    # This doesn't block.
   obj_ref = my_function.remote(random.random(), f"Goodbye for the {i}th time.")
   obj_refs.append(obj_ref)

# wait for all of the tasks to complete and ensure they result in the expected
# list of values
assert ray.get(obj_refs) == [1, 1, 1, 1]