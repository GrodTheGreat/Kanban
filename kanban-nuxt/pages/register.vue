<template>
  <main>
    <form action="" method="post">
      <fieldset>
        <legend>Register</legend>
        <div class="form-input">
          <label for="email">Email</label>
          <input type="email" name="email" id="email" />
        </div>
        <div class="form-input">
          <label for="password">Password</label>
          <input type="password" name="password" id="password" />
        </div>
        <div class="form-input">
          <label for="password">Confirm Password</label>
          <input type="password" name="password" id="password" />
        </div>
        <button type="submit">Register</button>
      </fieldset>
    </form>
  </main>
</template>

<style scoped>
main {
  display: flex;
  justify-content: center;
}

form {
  width: 90%;
  max-width: 40rem;
}

fieldset {
  padding: 2rem;
}

.form-input {
  display: flex;
  flex-direction: column;
}
</style>
