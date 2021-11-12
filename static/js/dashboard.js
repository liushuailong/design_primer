const ref = Vue.ref;
const watch = Vue.watch;
const App = {
    data() {
        return {
        }
    },
    setup() {
        // test add function
        const counter = ref(0)
        const addOne = function () {
            counter.value++
        }

        // control profile center open/close
        const center_flag = ref(true)
        const open_center = function () {
            center_flag.value = !center_flag.value
        }

        // watch url change: #...
        // problem: cann`t watch the url change in-time
        // for now use watch click event to change page
        cur_page = ref("dashboard")
        if (!(this.location.hash && !this.location.hash.startsWith("#"))) {
            cur_page.value = this.location.hash.replace("#", "")
        }
        const change_page = function (page_name) {
            cur_page.value = page_name
            console.log(cur_page.value)
        }



        return {
            addOne,
            counter,
            open_center,
            center_flag,
            cur_page,
            change_page,
        }
    }
}

// const routes = []
//
// const router = VueRouter.createRouter({
//   // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
//   history: VueRouter.createWebHashHistory(),
//   routes, // short for `routes: routes`
// })
Vue.createApp(App).mount("#app")