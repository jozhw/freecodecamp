const express = require("express");
const app = express();
const cors = require("cors");
require("dotenv").config();

const mongoose = require("mongoose");

mongoose.connect(process.env.MONGO_URI, () => {
  console.log("Connected to database succesfully");
});

app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/views/index.html");
});

const userSchema = mongoose.Schema(
  {
    username: {
      type: String,
      required: true,
    },
  },
  { versionKey: false }
);

// Schemas

// user schema
const User = mongoose.model("User", userSchema);

// exercise schema
const exerciseSchema = mongoose.Schema({
  username: { type: String, required: true },
  description: { type: String },
  duration: { type: Number },
  date: { type: Date },
  userId: { type: String },
});

const Exercise = mongoose.model("Exercise", exerciseSchema);

// POST to /api/users/:_id/exercises
app.post("/api/users/:_id/exercises", async (req, res) => {
  const foundUser = await User.findById(req.params._id);
  let {description, duration, date} = req.body;

  if (!foundUser) {
    return res.send({ error: "The ID provided is not associated with a user" });
  }
  
  // handle date
  if (!date) {
    date = new Date();
  } else {
    date = new Date(date)
  }
  
  const exercise = await Exercise.create({
    username: foundUser.username,
    description: description,
    duration: parseInt(duration),
    date: date.toDateString(),
    userId: req.params._id
  })

  return res.send({
    username: foundUser.username,
    description: description,
    duration: parseInt(duration),
    date: date.toDateString(),
    _id: req.params._id,
  });
});


// POST to /api/users username
app.post("/api/users", async (req, res) => {
  const username = req.body.username;
  const foundUser = await User.findOne({ username: username });

  if (foundUser) {
    return res.json(foundUser);
  }

  const user = await User.create({
    username: username,
  });

  res.json(user);
});

// GET request to /api/users for all users
app.get("/api/users", async (req, res) => {
  const users = await User.find();
  res.send(users);
});


// GET request to /api/users/:_id/logs
app.get('/api/users/:_id/logs', async (req, res) => {
  const userId = req.params._id;
  let {from, to, limit } = req.query;
  const userName = await User.findById(userId);
  
  let filter = {userId: userId};
  let dateFilter = {};
  
  if (from) {
    dateFilter["$gte"] = new Date(from);
  }
  if (to) {
    dateFilter["$lte"] = new Date(to)
  }
  
  if (from || to) {
    filter.date = dateFilter
  }
  
  if (!limit){
    limit = 100;
  }
  
  
  let logs = await Exercise.find(filter).limit(limit);
  
  
  
  
  logs = logs.map((exercise) => {
    return {
      description: exercise.description,
      duration: exercise.duration,
      date: exercise.date.toDateString()
    }
  })
  
  if (!userName){
    return res.send({"error": "User not found"})
  }
  
  if (!logs){
    return res.send({"error": "No logs found"})
  }
  
  const count = logs.length;
  
  res.json({
    username: userName.username,
     count: count,
    _id: userId,
    log: logs
    
  })
  

   
  
})


// POST request to /api/users/:_id/exercises
app.post("/api/users/:_id/exercises", async (req, res) => {
  const id = req.params._id;
});

const listener = app.listen(process.env.PORT || 3000, () => {
  console.log("Your app is listening on port " + listener.address().port);
});
