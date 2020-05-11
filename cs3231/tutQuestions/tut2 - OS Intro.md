# Operation Systems Introduction

1. What are some of the differences between a processor running in **privileged/kernel mode** vs **user mode**. Why do we need two nodes.

Kernel mode allows the processor to freely manage:

- Memory Allocation
- Switch Tasks
- Write/Write/Execute

Kernel mode is trusted to run programms while if a user wishes to do any of the above, it must go through many checks before it is allowed to be run by the operator.
