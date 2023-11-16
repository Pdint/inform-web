const userActionGroup = document.querySelector('.user-action-group');
const myMenuTrigger = userActionGroup.querySelector('.dropdown-button');
const myMenuContent = userActionGroup.querySelector('.dropdown-content');

const handleMyMenu = (event) => {
    myMenuContent.classList.toggle('is-active');
    myMenuTrigger.classList.toggle('is-active');
  };

  const init = () => {
    myMenuTrigger.addEventListener('click', handleMyMenu);
  };
  
  init();