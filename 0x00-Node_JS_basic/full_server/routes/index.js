import express from 'express';

const router = express.Router();

router.get('/', (req, res) => {
  res.render(AppController);
})

router.get('/students', (req, res) => {
  res.render(StudentController.getAllStudents());
})

router.post('/students/:major', (req, res) => {
  res.render(StudentController.getAllStudentsByMajor(major));
})

module.exports = router;
