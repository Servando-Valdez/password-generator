<script setup lang="ts">

</script>

<template>
    <div>
        <form>
            <div style="margin-top: 10px;margin-bottom: 10px;">
                <p class="text-center" style="margin-top: 10px;">Create strong and secure passwords.</p>
            </div>
            <div class="d-flex justify-content-evenly" style="margin-top: 10px;margin-bottom: 10px;">
                <div class="col-9"><input class="form-control" type="text" style="border-radius: 15px;"></div>
                <div class="col-2 d-flex justify-content-center align-content-center"><button class="btn btn-primary" type="button" style="border-radius: 40px;border-style: none;background: rgb(44,62,80);">Copy</button></div>
            </div>
            <div class="d-flex justify-content-evenly" style="margin-top: 10px;margin-bottom: 10px;">
                <div class="col-3"><input class="form-control" type="number" id="number-range" style="border-radius: 15px;"></div>
                <div class="col-5"><input class="form-range" type="range" id="range-password" style="--bs-primary: #2c3e50;--bs-primary-rgb: 44,62,80;color: rgb(44,62,80);"></div>
            </div>
            <div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="formCheck-1">
                    <label class="form-check-label" for="formCheck-1">Symbols</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="formCheck-2">
                    <label class="form-check-label" for="formCheck-2">Numbers</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="formCheck-3">
                    <label class="form-check-label" for="formCheck-3">Uppercase</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="formCheck-4">
                    <label class="form-check-label" for="formCheck-4">LowerCase</label>
                </div>
            </div>
            <div class="text-center"><button class="btn btn-primary" type="button" style="color: rgb(255,255,255);background: rgb(44,62,80);border-radius: 10px;padding: 12px;margin-top: 20px;border-style: none;">Generate Password</button></div>
        </form>
    </div>
</template>
