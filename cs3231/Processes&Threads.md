# Processes and Threads

## Their difference.

A process is a task/job, a single individual program.

A process has it's own allocated resources, and therefore, it cannot access another process's resources.

A process can have multiple threads.

### The thread model

A thread is a unit of execution and belongs to a process.

A thread can access the memory of another thread within the same process.

Local variables are per thread (allocated on the stack)

Global variables are shared between threads

Dynamically allocated memory can be global or local (program defined)

## Processes/Threads with the OS

The fundamental requirement of an OS is the interweave the execution of several processes in order to maximise the processor utilisation.

The OS also allocates resources required by processes, support communication between processes and user creation of processes.

Different OS perform such an requirement differently. For example:

- MSDOS uses a single process and a single thread
- OS/161 uses a single process and multiple threads
- Tradition UNIX uses multiple processes which have a single thread
- Modern UNIX (Linux) and Windows uses multiple processors and multiple threads

## Process Creation

Events which could trigger process creation

1. System Initilisation (Foreground or background processes)
2. Execution of a process creation system call (written within the executing code)
3. User Request
4. Initialisation of a batch job

## Process termination

1. Normal Exit (After the code has finished executing, voluntary)
2. Error Exit (Early exit on code error, voluntary)
3. Fatal Error (Involuntary)
4. Killed by another process (Involuntary)

## Process Control Block (PCB)

This is where information about a process is stored, forming a process table. It can store information about regiters, stack pointer, processID..etc.

## Process/Thread States

3 states exist:

- Running
- Ready
- Blocked

The scheduler/dispatcher chooses a "ready" process to run. Ready process line up in a queue to be run.

There is also a blocked queue.

## Thread or Process?

Threads are simpler to program.

Less resources associated. Cheap to create and destroy

Threads can take advantage of parallelism available on machines with more than one CPU.
