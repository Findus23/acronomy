const letterform = document.getElementById("letterform")!;

const letters = document.querySelectorAll("#letterselect span") as NodeListOf<HTMLSpanElement>
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
    const inputForm = document.getElementById("id_acro_letters")! as HTMLInputElement;
    inputForm.value = result.join(",");
});
const inButton = document.getElementById("initials")! as HTMLButtonElement;
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

export {}
