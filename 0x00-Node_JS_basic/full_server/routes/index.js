const express = require('express');
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

const router = express.Router();

router.get('/', (req, res) => {
  res.render(AppController);
})

router.get('/students', (req, res) => {
  res.render(StudentsController.getAllStudents());
})

router.post('/students/:major', (req, res) => {
  res.render(StudentsController.getAllStudentsByMajor(major));
})

module.exports = router;
