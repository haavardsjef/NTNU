/* Part 2 */
console.log('PART 2')

for (let i = 1; i < 21; i++) {
    console.log(i);    
}

/* Part 3 */
console.log('PART 3')

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 3 === 0) {
        console.log("eple");
    }
    else if (numbers[i] % 5 === 0) {
        console.log("kake");
    }
    else{
        console.log(numbers[i]);
    }
}

/* Part 4 */

document.getElementById("title").innerHTML = "Hello JavaScript"

/* Part 5 */
function changeDisplay () {
    const magic = document.getElementById("magic");
    magic.style.display = "none";
}

function changeVisibility () {
    const magic = document.getElementById("magic");
    magic.style.visibility = "hidden";
    magic.style.display = "block";
}

function reset () {
    const magic = document.getElementById("magic");
    magic.style.visibility = "visible";
    magic.style.display = "block";
}

/* Part 6 */
const technologies = [
    'HTML5',
    'CSS3',
    'JavaScript',
    'Python',
    'Java',
    'AJAX',
    'JSON',
    'React',
    'Angular',
    'Bootstrap',
    'Node.js'
];

const tech = document.getElementById("tech");

technologies.forEach(technology => {
    const listItem = document.createElement("li");
    listItem.appendChild(
      document.createTextNode(technology)
    );
    tech.appendChild(listItem);
});