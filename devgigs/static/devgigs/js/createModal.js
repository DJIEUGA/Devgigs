document.addEventListener('DOMContentLoaded', () => {
    //  When the DOM is ready, call functions
    control_modal()
})


function control_modal() {

    // Target button to create new gigs
    const openModal = document.querySelector('#create-btn')
    const modal = document.querySelector('.create-modal')
    const closeModal = document.querySelector('.close')

    // o
    openModal.onclick = () => {
        openModal.setAttribute('disabled', 'true')
        modal.style.display = 'block'
        document.querySelector('.modal-backdrop').style.display = 'block'
    }

    // close modal
    closeModal.onclick = () => {
        openModal.removeAttribute('disabled')
        modal.style.display = 'none'
        document.querySelector('.modal-backdrop').style.display = 'none'
    }

}