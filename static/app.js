document.addEventListener('DOMContentLoaded', function () {

    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'))
    const tooltipList = tooltipTriggerList.map(
        tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl)
    )

    new Autocomplete('#autocomplete', {
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

        onSubmit: result => {
            window.location = "/acronym/" + result.slug
        },
        autoSelect: true,
    })
    const input = document.querySelector('input[name="tags"]')
    if (input) {
        input.classList.remove("form-control")

        document.querySelector("form").addEventListener("submit", function () {
            const list = JSON.parse(input.value).map(function (item) {
                return item['value'];
            })
            input.value = list.join(",")
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
    }
    if (typeof CodeMirror !== "undefined") {
        const myCodeMirror = CodeMirror.fromTextArea(
            document.getElementById("id_description_md"),
            {
                lineWrapping: true,
                lineNumbers: true,
            }
        );
    }
    const letterform = document.getElementById("letterform");
    if (letterform) {
        console.log("found form")
        const letters = document.querySelectorAll("#letterselect span")
        letters.forEach(function (letter) {
            letter.addEventListener("click", function (e) {
                letter.classList.toggle("als")
            })
        })
        letterform.addEventListener("submit", function (e) {
            const result = [];
            for (let i = 0; i < letters.length; i++) {
                const el = letters[i];
                if (el.classList.contains("als") && el.innerText !== " ") {
                    result.push(i);
                }
            }
            const inputForm = document.getElementById("id_acro_letters");
            inputForm.value = result.join(",");
        });
        const inButton = document.getElementById("initials");
        inButton.addEventListener("click", function () {
            letters.forEach(function (el) {
                const content = el.innerText
                if (content !== content.toLowerCase()) {
                    el.classList.add("als")
                } else {
                    el.classList.remove("als")
                }

            })
        });
    }
})
