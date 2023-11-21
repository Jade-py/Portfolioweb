var typed = new Typed(".typing",{
    strings:["","Backend Developer"],
    typeSpeed:150,
    BackSpeed:80,
    loop:true
})

const myShow1btn = document.getElementById("myFirst");
const myShow2btn = document.getElementById("mySecond");
const myShow3btn = document.getElementById("myThird");
const sectionFirst = document.getElementById("nav1");
const sectionSecond = document.getElementById("nav2");
const sectionThird = document.getElementById("nav3");

myShow1btn.addEventListener("click", () => {
    sectionFirst.classList.add("fa-solid");
    sectionSecond.classList.remove("fa-solid");
    sectionThird.classList.remove("fa-solid");

  })

  myShow2btn.addEventListener("click", () => {
    sectionFirst.classList.remove("fa-solid");
    sectionSecond.classList.add("fa-solid");
    sectionThird.classList.remove("fa-solid");

  })

  myShow3btn.addEventListener("click", () => {
    sectionFirst.classList.remove("fa-solid");
    sectionSecond.classList.remove("fa-solid");
    sectionThird.classList.add("fa-solid");

  })
  document.addEventListener("DOMContentLoaded", function() {
    const scrollButton = document.getElementById("scrollButton");

    scrollButton.addEventListener("click", function() {
        const sectionToScrollTo = document.getElementById("contact"); // Change this ID to the section you want to scroll to
        sectionToScrollTo.scrollIntoView({ behavior: "smooth" });
    });
});
document.addEventListener("DOMContentLoaded", function() {
  const scrollButton = document.getElementById("scrollButton2");

  scrollButton.addEventListener("click", function() {
      const sectionToScrollTo = document.getElementById("contact"); // Change this ID to the section you want to scroll to
      sectionToScrollTo.scrollIntoView({ behavior: "smooth" });
  });
});