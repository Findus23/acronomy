import {basicSetup, EditorView} from "codemirror"
import {markdown} from "@codemirror/lang-markdown"

const textarea = document.getElementById("id_description_md")! as HTMLTextAreaElement
let editor = new EditorView({
    doc: textarea.value,
    extensions: [basicSetup, markdown()],
})
textarea.parentNode!.insertBefore(editor.dom, textarea)
textarea.style.display = "none"
textarea.form?.addEventListener("submit", () => {
    textarea.value = editor.state.doc.toString()
})
