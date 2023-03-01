
// ============Animation services=============

const observer= new IntersectionObserver((entries)=>{
    entries.forEach((entry)=>{
        if (entry.isIntersecting){
            entry.target.classList.add('show')
        }else{
            entry.target.classList.remove('show') 
        }
    })
});


const hiddenElements=document.querySelectorAll(".hidden");
hiddenElements.forEach((el)=> observer.observe(el));

// ==============Animation form==============
function _(e){
    return document.getElementById(e)
}

const partForm=_("partForm");
const entrForm=_("entrForm");
const btnPart=_("btnPart");
const btnEntr=_("btnEntr");
const cntForm=_("cntForm");

btnEntr.addEventListener('click', () => {
    btnPart.classList.remove('active');
    btnEntr.classList.add('active');
    if (entrForm.classList.contains("cacher")){
        entrForm.classList.remove("cacher");
        entrForm.classList.add("color");
        partForm.classList.add("cacher");
        // cntForm.style.transform='translate(-100%)'
        cntForm.style.transition='transform 0.5s'
    }
})

btnPart.addEventListener('click', () => {
    btnEntr.classList.remove('active');
    btnPart.classList.add('active');
    if (partForm.classList.contains("cacher")){
        partForm.classList.remove("cacher");
        entrForm.classList.add("cacher");
        // cntForm.style.transform='translate(0%)'
        cntForm.style.transition='transform 0.5s'
    }
})


