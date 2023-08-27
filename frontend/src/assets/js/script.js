
// let numberRange = document.getElementById('number-range');

// let rangeNumber = document.getElementById('range-password');

// rangeNumber.addEventListener('input', function(){
//     numberRange.value = rangeNumber.value
// })

// numberRange.addEventListener('input', function(event){
//     const maxAllowedValue = 50;
//     let inputValue = event.target.value;

//     if (inputValue > maxAllowedValue) {
//         inputValue = maxAllowedValue;
//     }

//     event.target.value = inputValue;
// })

// function addRange(){
//     rangeNumber.min = 1;
//     rangeNumber.max = 50;

//     numberRange.min = 1;
//     numberRange.max = 50;

//     rangeNumber.value = 12;
//     numberRange.value = rangeNumber.value;
// }

// addRange()

const checkboxes = document.querySelectorAll('input[type="checkbox"]');

for (const checkbox of checkboxes) {
  checkbox.addEventListener('click', function() {
    if (!this.checked && allUnchecked()) {
      this.checked = true;
    }
  });
}

function allUnchecked() {
  for (const checkbox of checkboxes) {
    if (checkbox.checked) {
      return false;
    }
  }
  return true;
}



