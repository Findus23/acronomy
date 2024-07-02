import Autocomplete from "@trevoreyre/autocomplete-js"

interface AutocompleteResult {
    url: string
    name: string
    full_name: string
    slug: string
}

new Autocomplete('#autocomplete', {
    search: (input: string) => {
        const acroSearch = input.split(':')[0];
        const url = "/api/acronym/?search=" + acroSearch

        return new Promise(resolve => {
            if (acroSearch.length < 1) {
                return resolve([])
            }

            fetch(url)
                .then(response => response.json())
                .then((data:AutocompleteResult[]) => {
                    resolve(data)
                })
        })
    },

    getResultValue: (result:AutocompleteResult) => (result.name + ": " + result.full_name),

    onSubmit: (result:AutocompleteResult) => {
        window.location.href = "/acronym/" + result.slug
    },
    autoSelect: true,
})
