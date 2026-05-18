# Notification Priority System Design

## Objective

The goal is to maintain a Priority Inbox
that displays only the Top 10 important notifications.

---

# Approach

Each notification contains:

- ID
- Type
- Message

Priority is calculated based on:

1. Notification Type
2. Important keywords in message

Example:

- Placement notifications have higher priority
- Messages containing hiring or internship receive extra score

---

# Efficient Top 10 Maintenance

A Min Heap is used to efficiently maintain Top 10 notifications.

Algorithm:

1. Traverse notifications
2. Calculate priority
3. Insert into Min Heap
4. Remove smallest element if heap size exceeds 10

This ensures only Top 10 notifications remain.

---

# Time Complexity

Sorting all notifications:

O(N log N)

Using Min Heap:

O(N log 10)

Approximately O(N)

---

# Data Structures Used

- Heap Queue
- Dictionary
- List

---

# Conclusion

The system efficiently prioritizes notifications
using Min Heap optimization.