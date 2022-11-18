var HeightInput = document.querySelector(".Height-input-field");
var WeightInput = document.querySelector(".Weight-input-field");
var calculateButton = document.querySelector(".calculate");
var result = document.querySelector(".result");
var statement = document.querySelector(".result-statement");
var BMI, Height, Weight;

calculateButton.addEventListener("click", ()=>{

    Height = HeightInput.value;
    Weight = WeightInput.value;
    BMI = Weight/(Height**2); 
    result.innerText = BMI;

    if(BMI < 18.5){
        statement.innerText = "Your BMI falls within the underweight range";    
    }else if((BMI > 18.5) && (BMI < 24.9)){
        statement.innerText = "Your BMI falls within the normal or healthy weight range";
    }else if((BMI > 25) && (BMI < 29.9 )){
        statement.innerText = "Your BMI falls within the overweight range";
    }else{
        statement.innerText = "Your BMI falls within the obese range";
    }
});
