//opens modal for projects
function openModal(number){
    var modalP = document.getElementById('modalP');
    modalP.textContent = "This is where the extended version of the description of Project "+ number +" should go. This project is a wonderful project that this fellow has worked very hard on, using these technologies, to create this effect."
    modalP.style.color = "black";
    
    var modal = document.getElementById("projectModal");
    modal.style.display = "block";
  
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function() {
        modal.style.display = "none";
    }
  
    window.onclick = function(event) {
        if (event.target == modal) {
                modal.style.display = "none";
        }
    }
  
  }
  