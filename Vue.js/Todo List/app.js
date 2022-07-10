const { createApp, ref, onMounted, computed } = Vue

// Nisheet Patel
// Date : 10/7/2022

createApp({
    setup() {
        const Cselect = ref({
            'all': true,
            'comp': false,
            'uncomp': false
        })

        const inputtext = ref('')
        const todos = ref({})
        const count = ref(0)

        // Make Button Exclusive
        function fselect(name) {

            Cselect.value = {
                'all': false,
                'comp': false,
                'uncomp': false
            }

            Cselect.value[name] = true
        }

        // Storing Data into local storage
        async function storeData() {
            localStorage.setItem("TodoList", JSON.stringify(todos.value))
            localStorage.setItem("TodoCount", count.value.toString())
        }

        // Add new todo 
        function newToDo() {
            if (inputtext.value == '') return

            todos.value[count.value++] = {
                "title": inputtext.value,
                "checked": false
            }

            inputtext.value = ''

            storeData()

        }

        // remove todo
        function removeToDo(id) {
            delete todos.value[id]
            storeData()
        }

        // strike through
        function toggleStrike(id) {
            try {
                todos.value[id].checked = !todos.value[id].checked
                storeData()
            } catch (error) {
                return
            }

        }

        // Filter Json Object
        Object.filter = (obj, predicate) =>
            Object.keys(obj)
                .filter(key => predicate(obj[key]))
                .reduce((res, key) => (res[key] = obj[key], res), {});

        // filtered todos to display 
        const filteredTodos = computed(() => {

            if (Cselect.value['all']) {
                return todos.value
            }

            return Cselect.value['comp']
                ? Object.filter(todos.value, todo => todo.checked == true)
                : Object.filter(todos.value, todo => todo.checked == false)
        })

        // 
        onMounted(() => {

            todos.value = JSON.parse(localStorage.getItem('TodoList'))
            co = parseInt(localStorage.getItem('TodoCount'))
            if (!isNaN(co)) {
                count.value = co
            }
            else {
                count.value = 0
                todos.value = {}
            }
        })


        return {
            Cselect,
            inputtext,
            fselect,
            newToDo,
            removeToDo,
            toggleStrike,
            filteredTodos
        }
    }
}).mount('#app')