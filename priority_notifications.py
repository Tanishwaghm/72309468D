import heapq

# Sample notification data
notifications = [
    {
        "ID": 1,
        "Type": "Placement",
        "Message": "CSX Corporation hiring"
    },
    {
        "ID": 2,
        "Type": "Result",
        "Message": "mid-sem results declared"
    },
    {
        "ID": 3,
        "Type": "Event",
        "Message": "tech-fest registration open"
    },
    {
        "ID": 4,
        "Type": "Placement",
        "Message": "Advanced Micro Devices Inc. hiring"
    },
    {
        "ID": 5,
        "Type": "Result",
        "Message": "project-review schedule"
    },
    {
        "ID": 6,
        "Type": "Event",
        "Message": "farewell event"
    },
    {
        "ID": 7,
        "Type": "Placement",
        "Message": "external hiring drive"
    },
    {
        "ID": 8,
        "Type": "Result",
        "Message": "exam results announced"
    },
    {
        "ID": 9,
        "Type": "Event",
        "Message": "coding competition"
    },
    {
        "ID": 10,
        "Type": "Placement",
        "Message": "internship opportunity"
    },
    {
        "ID": 11,
        "Type": "Event",
        "Message": "sports tournament"
    }
]

# Priority score for notification types
type_priority = {
    "Placement": 50,
    "Result": 40,
    "Event": 30
}

# Function to calculate priority
def calculate_priority(notification):

    score = type_priority.get(notification["Type"], 0)

    message = notification["Message"].lower()

    if "hiring" in message:
        score += 20

    if "results" in message:
        score += 15

    if "internship" in message:
        score += 10

    return score


# Function to maintain top 10 notifications
def get_top_notifications(notification_list, top_k=10):

    min_heap = []

    for notification in notification_list:

        priority = calculate_priority(notification)

        item = (priority, notification)

        if len(min_heap) < top_k:

            heapq.heappush(min_heap, item)

        else:

            if priority > min_heap[0][0]:

                heapq.heappop(min_heap)

                heapq.heappush(min_heap, item)

    return sorted(min_heap, reverse=True)


# Main
top_notifications = get_top_notifications(notifications)

print("\nTOP 10 PRIORITY NOTIFICATIONS\n")

for rank, (score, notification) in enumerate(top_notifications, start=1):

    print(f"Rank #{rank}")
    print(f"Priority Score : {score}")
    print(f"ID             : {notification['ID']}")
    print(f"Type           : {notification['Type']}")
    print(f"Message        : {notification['Message']}")
    print("-" * 40)