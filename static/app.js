$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})


new Autocomplete('#autocomplete', {

    // Search function can return a promise
    // which resolves with an array of
    // results. In this case we're using
    // the Wikipedia search API.
    search: input => {

        const acroSearch = input.split(':')[0];
        const url = "/api/acronym/?search=" + acroSearch

        return new Promise(resolve => {
            if (acroSearch.length < 1) {
                return resolve([])
            }

            fetch(url)
                .then(response => response.json())
                .then(data => {
                    resolve(data)
                })
        })
    },

    getResultValue: result => (result.name + ": " + result.full_name),

    // Open the selected article in
    // a new window
    onSubmit: result => {
        console.log(result)
        window.location = "/acronym/" + result.slug
    },
    autoSelect: true,
})
const input = document.querySelector('input[name="tags"]')
input.classList.remove("form-control")

document.querySelector("form").addEventListener("submit", function () {
    const list = JSON.parse(input.value).map(function (item) {
        return item['value'];
    })
    input.value = JSON.parse(input.value).map(function (item) {
        return item['value'];
    })
    console.log(input.value)
    return false;
})
const tagify = new Tagify(input, {
    whitelist: [],
    maxTags: 10,
    dropdown: {
        maxItems: 20,
        enabled: 0
    }
})
fetch("/api/tag/")
    .then(response => response.json())
    .then(data =>
        data.map(function (item) {
            return item['name'];
        })
    )
    .then(data => {

        tagify.settings.whitelist = data

    })

const myCodeMirror = CodeMirror.fromTextArea(
    document.getElementById("id_description_md"),
    {
        lineWrapping: true,
        lineNumbers: true,
    }
);
