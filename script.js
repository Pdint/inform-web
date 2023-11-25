document.addEventListener("DOMContentLoaded", function () {
  // 선택한 데이터에 대한 API 호출 및 결과 표시
  document.getElementById("select").addEventListener("change", function () {
    const selectedValue = this.value;
    fetchData(selectedValue);
  });

  // 버튼 클릭 시에도 정보 송출
  document.getElementById("submitButton").addEventListener("click", function () {
    const selectedValue = document.getElementById("select").value;
    fetchData(selectedValue);
  });

  // document 클릭 시 결과 영역 숨김
  document.addEventListener("click", function (event) {
    const resultDiv = document.getElementById("result");

    // 클릭된 요소가 결과 영역이나 관련 요소인지 확인
    if (!resultDiv.contains(event.target) && event.target.id !== "select" && event.target.id !== "submitButton") {
      // 결과 영역 숨기기
      resultDiv.style.display = "none";
    }
  });
});

function fetchData(userId) {
  // 가짜 API URL (JSONPlaceholder 사용)
  const apiUrl = `https://jsonplaceholder.typicode.com/posts/${userId}`;

  // API 호출
  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      // API 결과를 처리하여 HTML에 추가
      displayResult(data);
    })
    .catch(error => {
      console.error("API 호출 중 오류 발생:", error);
    });
}

function displayResult(data) {
  // 이미지를 표시할 img 요소
  const userImage = document.getElementById("userImage");
  // 결과를 표시할 div
  const userInfoDiv = document.getElementById("userInfo");
  // 결과를 표시할 div
  const resultDiv = document.getElementById("result");

  // 이전에 표시된 내용 지우기
  userInfoDiv.innerHTML = "";

  // 이미지 URL이 있다면 이미지 표시
  if (data.hasOwnProperty("image")) {
    userImage.src = data.image;
    userImage.style.display = "block";
  } else {
    userImage.style.display = "none";
  }

  // 결과를 텍스트로 변환하여 표시
  for (const key in data) {
    if (data.hasOwnProperty(key) && key !== "image") {
      const paragraph = document.createElement("p");
      paragraph.innerHTML = `<strong>${key}:</strong> ${data[key]}`;
      userInfoDiv.appendChild(paragraph);
    }
  }

  // 결과 영역 보이기
  resultDiv.style.display = "block";
}
