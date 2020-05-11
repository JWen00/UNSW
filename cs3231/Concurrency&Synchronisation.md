# Concurrency

Whilst we a led to believe that the CPU spends all its time running what it tell it to run, it's actually switching from task to task so quickly we can hardly perceive it.

This means that while it's running your program, it might stop at line 90, run another program's line 203 and then come back to line 91 like nothing happened.

However if during the time it is away, the resource which was supposed to be update was changed by another program?

## Critical Region

A critical region is a region of code where shared resources are accessed. (Variables, memory, files..etc)

Uncoordinated entry into such critical regions result in a **race condition**. This may cuase incorrect or unexpected behaviour like deadlocks, or lost work from updating the wrong version.

### Solution?

1. Mutual Exclusion
2. No assumptions made about the speed or number of CPUs
3. No process outside the critical region may block another process.
4. No process waits forever to enter the critical region

### Solution | Lock

We can create a lock variable.

If lock == 1, someonebody is in the region and we wait

If lock == 0, the critical region is free to enter

**Problem**: The the lock may be considered "free" when it is not as the program is context switched before the lock can be locked.

### Solution | Taking turns

Each process takes turns.

```
while (true) {
    while (turn != 0) {
        critical_region();
        turn = 1;
        non_critical_region();
    }
}
```

This can be bad because of the busy waiting - when the process must wait even though the other process is doing something else.

The solution is particularly bad when processes require the critical sections at different rates (one may need it for much longer than another).

### Solution | Mutual Exclusion with Test-and-Set

We can use hardware support to guaruntee mutual exclusion. The test-and-set instruction can be used to implement lock variables.

It loads the value of the lock and if false, we set it at the same time to aqcuire the lock, else return. The hardware guarantees that the instruction can execute atomically.

Test-and-Set is simple and available at user-level.

However it does lots of busy-waits and hence consumes CPU. There could also be more than one process waiting.

### Solution | Sleep/Wakeup

We can tackle the busy wait problem by putting a process to sleep and calling it to wake up when the critical region is free.

## Producer consumer bounded buffer problem

The bounded buffer problem refers to when

> A producer produces data items and stores the items into a buffer.
>
> A consumer takes the items out of the buffer and consumes them.

We must keep track of the number of items in the buffer.

The producer should sleep when the buffer is full and wakeup when there is empty space in the buffer.

The consumer, conversely should sleep when the buffer is empty, and

Can watch a video on it. Much better than however I would explain it haha.

## Semaphores

Semaphores were introduced by Dijkstra (1965).

P() -> Proberen meaning **to test**

V() -> Verhogen meaning **to increment**

If a resource isn't available, the corresponding sempaore blocks any process waiting for the resource.

The blocked processes are put into a process queue maintained by the sempaphore

When a process releases a resource, it signals by changing the value of the semaphore.

Signally resumes a blocked process in the queue (if any)

Complex coordination can be implemented by multiple semaphores.

Consider two simple operations: wait(S) and signal(S)

```
wait(S) {
    S.count--;
    if (S.count < 0 ) {
        Add process to S.list;
        sleep;
    }
}

signal(S) {
    S.count++;
    if (S.count <= 0) {
        remove a process P from S.list;
        wakeup(P);
    }
}
```

We can use semaphores to solve the producer-consumer problem as it also allows us to keep track of the number of items within the buffer.
