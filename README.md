# **Task-Schedular**

## **How to Use? ⚙️**

### Task you can perform

| Action     |     | Description                      |
| ---------- | --- | -------------------------------- |
| openApp    | --> | To open app at schedule time     |
| openUrl    | --> | To open url at schedule time     |
| runCommand | --> | Execute command at schedule time |

### **How to schedule?**

```json
[
  {
    "task_name": "Open VS code",
    "Action": "openApp",
    "args": "C://Program Files//Microsoft VS Code//Code.exe",
    "schedule": {
      "type": "daily",
      "time": "09:00"
    }
  },
  {
    "task_name": "Open YouTube",
    "Action": "openUrl",
    "args": "https://www.youtube.com/",
    "schedule": {
      "type": "date",
      "date": "2023-04-18",
      "time": "15:06"
    }
  },
  {
    "task_name": "Run a script",
    "Action": "runCommand",
    "args": "python script.py",
    "schedule": {
      "type": "date",
      "date": "2023-04-22",
      "time": "11:00"
    }
  }
]
```