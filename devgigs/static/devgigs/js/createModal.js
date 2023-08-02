document.addEventListener('DOMContentLoaded', () => {
    //  When the DOM is ready, call functions
    control_modal()
})


function control_modal() {

    // Target button to create new gigs
    const openModal = document.querySelector('#create-btn')
    const modal = document.querySelector('.create-modal')
    const closeModal = document.querySelector('.close')

    openModal.onclick = () => {
        document.querySelector('#form-modal').setAttribute('method', 'post')
        document.querySelector('#form-modal').setAttribute('action', '/create')
        document.querySelector('#form-modal').setAttribute('enctype', 'multipart/form-data')
        document.querySelector('#modal-heading').innerHTML = 'Create a Gig'
        document.querySelector('#modal-subheading').innerHTML = 'Post a gig to find a developer'
        document.querySelector('#form-save-btn').innerHTML = 'Create'
        openModal.setAttribute('disabled', 'true')
        modal.style.display = 'block'
        document.querySelector('.modal-backdrop').style.display = 'block'

        console.log(document.querySelector('#form-modal').getAttribute('method'))
    }

    // close modal
    closeModal.onclick = () => {
        document.querySelector('#create-btn').removeAttribute('disabled')
        modal.style.display = 'none'
        document.querySelector('.modal-backdrop').style.display = 'none'
    }

}