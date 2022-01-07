import express from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

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
