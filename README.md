# **Task-Schedular**

## **How to Use? ⚙️**

### Task you can perform

| Action     |     | Description                      |
| ---------- | --- | -------------------------------- |
| openApp    | --> | To open app at schedule time     |
| openUrl    | --> | To open url at schedule time     |
| runCommand | --> | Execute command at schedule time |

You can modify the "schedule_str" field in the task object to set different scheduling intervals:

### **For a one-time task:**

```json
{
    "task_name": "One-time task",
    "Action": "RunCommand",
    "args": "echo 'Hello, world!'",
    "schedule": "2023-04-19 10:30:00"  # Run on April 19th, 2023 at 10:30 AM
}
```

### **For a daily task:**

```json
{
    "task_name": "Daily task",
    "Action": "RunCommand",
    "args": "echo 'Good morning!'",
    "schedule": "08:00"  # Run every day at 8:00 AM
}
```

### **For a weekly task:**

```json
{
    "task_name": "Weekly task",
    "Action": "RunCommand",
    "args": "echo 'Happy Monday!'",
    "schedule": "monday 09:30"  # Run every Monday at 9:30 AM
}
```

### **For a monthly task:**

```json
{
    "task_name": "Monthly task",
    "Action": "RunCommand",
    "args": "echo 'Happy first of the month!'",
    "schedule": "1 12:00"  # Run on the 1st day of every month at noon
}
```
