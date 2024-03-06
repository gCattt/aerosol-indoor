function myFunction() {
    document.getElementById("csvBtn").classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.csvBtn')) {
      var dropdowns = document.getElementsByClassName("csvDrop");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

  $("#csvBtn").on("click", function(event){
      $(this).toggleClass("show");
  });