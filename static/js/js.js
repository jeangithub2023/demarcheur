const hanbugerOpen=document.querySelector(".hanbuger-open")
const hanbugerClose=document.querySelector(".hanbuger-close")
const menuLink=document.querySelector(".menuLink")
const sigin=document.querySelector(".btn-sigin")

hanbugerOpen.addEventListener('click',()=>{
    menuLink.classList.toggle("open")
    hanbugerOpen.classList.toggle("cacher")
    hanbugerClose.classList.toggle("vue")
    sigin.classList.toggle("open")
})
hanbugerClose.addEventListener('click',()=>{
    menuLink.classList.remove("open")
    hanbugerOpen.classList.remove("cacher")
    hanbugerClose.classList.remove("vue")
    sigin.classList.remove("open")
})
