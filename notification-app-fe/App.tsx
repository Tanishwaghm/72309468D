import "./styles.css";

function App() {

  const notifications = [
    {
      id: 1,
      type: "Placement",
      message: "CSX Corporation hiring",
      priority: 70
    },
    {
      id: 2,
      type: "Result",
      message: "mid-sem results declared",
      priority: 55
    },
    {
      id: 3,
      type: "Event",
      message: "tech-fest registration open",
      priority: 30
    }
  ];

  return (
    <div className="container">

      <h1>Priority Notifications</h1>

      {
        notifications.map((notification) => (

          <div className="card" key={notification.id}>

            <h2>{notification.type}</h2>

            <p>{notification.message}</p>

            <span>
              Priority Score: {notification.priority}
            </span>

          </div>
        ))
      }

    </div>
  );
}

export default App;