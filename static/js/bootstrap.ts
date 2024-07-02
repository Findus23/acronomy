import Dropdown from "bootstrap/js/dist/dropdown";
import Tooltip from "bootstrap/js/dist/tooltip";

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList]
    .map(tooltipTriggerEl => new Tooltip(tooltipTriggerEl))

const dropdownElementList = document.querySelectorAll('.dropdown-toggle')
const dropdownList = [...dropdownElementList].map(dropdownToggleEl => new Dropdown(dropdownToggleEl))
