export default function createReportObject(employeesList) {
  const dickie = {
    allEmployees: employeesList,
    getNumberOfDepartments() {
      return Object.keys(employeesList).length;
    },
  };
  return dickie;
}
