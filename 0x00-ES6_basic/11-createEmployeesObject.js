export default function createEmployeesObject(departmentName, employees) {
  const dicty = { [departmentName]: [...employees] };
  return dicty;
}
