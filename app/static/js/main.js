// preview & filename UI
const input = document.getElementById('imageInput');
const fileName = document.getElementById('fileName');
const previewImg = document.getElementById('previewImg');

if (input) {
  input.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (!file) {
      fileName.textContent = "No file chosen";
      return;
    }
    fileName.textContent = file.name;
    // show preview locally before upload (if preview area exists)
    if (previewImg) {
      previewImg.src = URL.createObjectURL(file);
    }
  });

  // allow clicking the upload box to open file picker
  const uploadBox = document.querySelector('.upload-box');
  if (uploadBox) {
    uploadBox.addEventListener('click', () => input.click());
  }
}
