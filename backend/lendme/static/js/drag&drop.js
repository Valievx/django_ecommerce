function applyDnDFile(el) {
  const beforeUploadEl = el.querySelector(".before-upload");
  const afterUploadEl = el.querySelector(".after-upload");
  const inputFile = el.querySelector("input[type='file']");
  const imagePreviewContainer = el.querySelector(".image-preview-container");
  const clearBtn = el.querySelector(".after-upload .clear-btn");

  function showImagePreviews(files) {
    imagePreviewContainer.innerHTML = ""; // Очищаем контейнер предварительного просмотра

    for (let i = 0; i < files.length; i++) {
      const img = document.createElement("img");
      const blobUrl = URL.createObjectURL(files[i]);
      img.src = blobUrl;
      imagePreviewContainer.appendChild(img);
    }

    afterUploadEl.style.display = "block";
    beforeUploadEl.style.display = "none";
  }

  beforeUploadEl.addEventListener("click", (e) => {
    e.preventDefault();
    inputFile.click();
  });

  inputFile.addEventListener("change", (e) => {
    e.preventDefault();
    showImagePreviews(e.target.files);
  });

  clearBtn.addEventListener("click", (e) => {
    afterUploadEl.style.display = "none";
    beforeUploadEl.style.display = "flex";
    imagePreviewContainer.innerHTML = ""; // Очищаем контейнер предварительного просмотра
  });

  beforeUploadEl.addEventListener("dragover", (e) => {
    e.preventDefault();
    el.classList.add("active");
  });

  beforeUploadEl.addEventListener("dragleave", (e) => {
    e.preventDefault();
    el.classList.remove("active");
  });

  beforeUploadEl.addEventListener("drop", (e) => {
    e.preventDefault();
    el.classList.remove("active");
    showImagePreviews(e.dataTransfer.files);
  });
}

applyDnDFile(document.querySelector(".file-dnd"));