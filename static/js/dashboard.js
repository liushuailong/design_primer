const ref = Vue.ref;
const watch = Vue.watch;
const App = {
    setup() {
        // control profile center open/close
        const center_flag = ref(true)
        const open_center = function () {
            center_flag.value = !center_flag.value
        }

        // watch url change: #...
        // problem: cann`t watch the url change in-time
        // for now use watch click event to change page
        cur_page = ref("dashboard")
        if (this.location.hash && !this.location.hash.startsWith("#")) {
            cur_page.value = this.location.hash.replace("#", "")
        }
        this.location.hash = "#dashboard"
        const change_page = function (page_name) {
            cur_page.value = page_name
            console.log(cur_page.value)
        }



        return {
            open_center,
            center_flag,
            cur_page,
            change_page,
        }
    }
}

Vue.createApp(App).mount("#app")