fun getImportance(employees: List<Employee?>, id: Int): Int {
    val idIndexMap = HashMap<Int, Employee>()
    employees.forEach { employee ->
        idIndexMap[employee!!.id] = employee
    }
    var totalImportance = 0

    val stack = Stack<Int>().apply {
        push(id)
    }

    while (stack.isNotEmpty()) {
        val currentEmployee = idIndexMap[stack.pop()]
        totalImportance += currentEmployee!!.importance
        for (e in currentEmployee.subordinates) {
            stack.push(e)
        }
    }


    return totalImportance
}
