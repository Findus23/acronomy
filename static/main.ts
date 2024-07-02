import 'vite/modulepreload-polyfill'
import "./js/autocomplete"
import "./js/bootstrap"

function init_edit(){
    if (document.querySelector('input[name="tags"]')) {
        import ("./js/tags").then(value => console.log("loaded"))
    }
    if (document.getElementById("id_description_md")) {
        import ("./js/codemirror").then(value => console.log("loaded"))
    }
    if (document.getElementById("letterform")) {
        import ("./js/letter").then(value => console.log("loaded"))
    }

}
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init_edit)
} else {
    init_edit()
}
