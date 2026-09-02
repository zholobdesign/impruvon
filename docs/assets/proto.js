
(function(){
  var KEY='impruvon-proto-notes';
  var btn=document.getElementById('notesToggle');
  function apply(on){
    document.body.classList.toggle('shownotes',on);
    if(btn) btn.textContent = on ? 'Hide notes' : 'Show notes';
  }
  var on=false;
  try{ on = localStorage.getItem(KEY)==='1'; }catch(e){}
  apply(on);
  if(btn) btn.addEventListener('click',function(){
    on=!on; apply(on);
    try{ localStorage.setItem(KEY,on?'1':'0'); }catch(e){}
  });
})();
