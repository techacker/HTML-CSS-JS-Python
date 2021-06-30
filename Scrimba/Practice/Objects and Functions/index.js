let person = {
    name: "Anurag",
    age: 43,
    country: "USA"
}

let age = 15

function logData() {
    let string = person.name + " is " + person.age + " years old and lives in " + person.country
    return string
}

if (age > 66) {
    console.log("senior citizens discount")
} else if (age > 27) {
    console.log("full price")
} else if (age > 18) {
    console.log("student discount")
} else if (age > 6) {
    console.log("child discount")
} else {
    console.log("free")
}