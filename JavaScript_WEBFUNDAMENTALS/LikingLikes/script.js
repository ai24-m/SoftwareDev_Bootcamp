// var add = 0
// var addElement = document.querySelector("p .add")

// function addlike(e){
//     e = document.querySelector("p .add")
//     console.log(e)
//     addElement.innerText = add ++
// }


function addlike(e){
    // console.log(e.parentElement.querySelector("p #add"));
    var addElement = e.parentElement.querySelector("p .add")
    var count =parseInt(addElement.innerText)
    // console.log(count)
    addElement.innerText= count=count + 1;
}

// function add(e){
//     var likes = e.parentElement.querySelector("p .likes")
//     let count = parentInt(likes.innerText)
//     likes.innerText= count +1
// }