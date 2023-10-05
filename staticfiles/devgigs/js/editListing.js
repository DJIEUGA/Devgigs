document.addEventListener('DOMContentLoaded', () => {
    //  When the DOM is ready, call functions
    edit_modal()
})


function edit_modal() {
    const list = document.querySelectorAll('.edit-btn')
    list.forEach(element => {

    });

    document.querySelectorAll('.edit-btn').forEach(listing => {
        listing.onclick = () => {

            // Populate each form fields with current information of the listing
            document.querySelectorAll('.listing-id').forEach((item) => {

                fetch(`/listing/${item.innerHTML}`)
                    .then(response => response.json())
                    .then(data => {
                        document.querySelector('#input-company').value = data.listing.company
                        document.querySelector('#input-title').value = data.listing.title
                        document.querySelector('#input-tags').value = data.listing.tags
                        document.querySelector('#input-description').value = data.listing.description
                        document.querySelector('#input-website').value = data.listing.website
                        document.querySelector('#input-email').value = data.listing.email
                        document.querySelector('#input-location').value = data.listing.location

                        // Update the form's method, action and enctype attributes
                        document.querySelector('#form-modal').setAttribute('method', 'post')
                        document.querySelector('#form-modal').setAttribute('action', `/edit/${item.innerHTML}`)
                        document.querySelector('#form-modal').setAttribute('enctype', 'multipart/form-data')
                    })

            })

            // Set the text of the form heading, subheading and submit btn of the edit form
            document.querySelector('#modal-heading').innerHTML = 'Edit Gig'
            document.querySelector('#modal-subheading').innerHTML = 'Edit: Job Title'
            document.querySelector('#form-save-btn').innerHTML = 'Save'

            // Set the attribute of the edit form
            listing.setAttribute('disabled', 'true')
            document.querySelector('#create-btn').setAttribute('disabled', 'true')
            document.querySelector('.create-modal').style.display = 'block'
            document.querySelector('.modal-backdrop').style.display = 'block'
        }
    });

    // close modal
    document.querySelector('.close').onclick = (e) => {
        document.querySelector('#create-btn').removeAttribute('disabled')
        document.querySelectorAll('.edit-btn').forEach(listing => {
            listing.removeAttribute('disabled')
        })

        document.querySelector('.create-modal').style.display = 'none'
        document.querySelector('.modal-backdrop').style.display = 'none'
    }

}
