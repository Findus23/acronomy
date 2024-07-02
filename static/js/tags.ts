import Tagify from '@yaireo/tagify'

interface Tag {
    name: string
}

interface Value {
    value: string
}

const input = document.querySelector('input[name="tags"]')! as HTMLInputElement
input.classList.remove("form-control")

document.querySelector("form")!.addEventListener("submit", function () {
    const rawData = JSON.parse(input.value) as Value[]
    const list = rawData.map(function (item) {
        return item.value;
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
    .then((data: Tag[]) =>
        data.map(function (item) {
            return item.name;
        })
    )
    .then(data => {
        tagify.settings.whitelist = data
    })

