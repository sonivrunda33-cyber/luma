import {toast} from '../core/ui.js';
import {setProfile} from '../core/utils.js';

export function init(){
  const form=document.querySelector('#profileForm');
  const name=localStorage.getItem('luma-profile-name')||'Alex Morgan';
  const goal=localStorage.getItem('luma-weekly-goal')||'12';
  document.querySelector('#settingName').value=name;document.querySelector('#settingGoal').value=goal;
  const reminder=document.querySelector('#reminderToggle');reminder.checked=localStorage.getItem('luma-reminders')==='true';
  form?.addEventListener('submit',event=>{event.preventDefault();const newName=form.elements.name.value.trim()||'Alex Morgan';const newGoal=Math.max(1,Math.min(100,Number(form.elements.goal.value)||12));localStorage.setItem('luma-profile-name',newName);localStorage.setItem('luma-weekly-goal',String(newGoal));setProfile(newName);toast('Preferences saved in this browser')});
  reminder?.addEventListener('change',()=>{localStorage.setItem('luma-reminders',String(reminder.checked));toast(reminder.checked?'In-app reminder preference enabled':'In-app reminder preference disabled')});
}
