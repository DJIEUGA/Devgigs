document.addEventListener('DOMContentLoaded', () => {
    //  When the DOM is ready, call functions
    edit_modal()
})


function edit_modal() {

    document.querySelector('#edit-btn').onclick = () => {

        // form attribute
        document.querySelector('#form-modal')
        document.querySelector('#modal-heading').innerHTML = 'Edit Gig'
        document.querySelector('#modal-subheading').innerHTML = 'Edit: Job Title'
        document.querySelector('#form-save-btn').innerHTML = 'Save'

        document.querySelector('#create-btn').setAttribute('disabled', 'true')
        document.querySelector('#edit-btn').setAttribute('disabled', 'true')
        document.querySelector('.create-modal').style.display = 'block'
        document.querySelector('.modal-backdrop').style.display = 'block'
        // get_listing(4)
    }

    // close modal
    document.querySelector('.close').onclick = (e) => {
        document.querySelector('#create-btn').removeAttribute('disabled')
        document.querySelector('#edit-btn').removeAttribute('disabled')

        document.querySelector('.create-modal').style.display = 'none'
        document.querySelector('.modal-backdrop').style.display = 'none'
    }

    const modal = document.querySelector('#modal-container')
    window.onclick = function (ev = new Event().target) {
        if (ev == modal) {
                document.querySelector('#create-btn').removeAttribute('disabled')
                document.querySelector('#edit-btn').removeAttribute('disabled')

                document.querySelector('.create-modal').style.display = 'none'
                document.querySelector('.modal-backdrop').style.display = 'none'
        }
        else {
            console.log("Clicking outside of modal will not close it!")
        }
    }

}

function get_listing(listingId) {
    fetch(`/listing/${listingId}`)
        .then(response => response.json())
        .then(data => {
            console.log({ "data": data })
        })
}