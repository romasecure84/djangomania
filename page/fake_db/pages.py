VISION_DETAIL = '''
<!-- cards -->
        <div class="card mb-3">
            <img src="https://picsum.photos/id/101/1200/200" class="card-img-top" alt="...">
            <div class="card-body">
                <p class="card-text">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Delectus, maiores porro
                    in quasi nihil tempore fugiat unde molestias ipsum repellendus, architecto autem nobis laudantium
                    eligendi! Nesciunt illo similique delectus accusamus?</p>
                <p class="card-text"><small class="text-body-secondary"></small></p>
            </div>
        </div>
        <img src="https://picsum.photos/id/99/1200/200" class="card-img-top" alt="...">
        <div class="card-body">
            <p class="card-text">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Delectus, maiores porro in
                quasi nihil tempore fugiat unde molestias ipsum repellendus, architecto autem nobis laudantium eligendi!
                Nesciunt illo similique delectus accusamus?</p>
            <p class="card-text"><small class="text-body-secondary"></small></p>
        </div>

        <img src="https://picsum.photos/id/98/1200/200" class="card-img-top" alt="...">
        <div class="card-body">
            <p class="card-text">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Delectus, maiores porro in
                quasi
                nihil tempore fugiat unde molestias ipsum repellendus, architecto autem nobis laudantium eligendi!
                Nesciunt
                illo similique delectus accusamus?</p>
            <p class="card-text"><small class="text-body-secondary"></small></p>
        </div>

        <img src="https://picsum.photos/id/102/1200/200" class="card-img-top" alt="...">
        <div class="card-body">
            <p class="card-text">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Delectus, maiores porro in
                quasi
                nihil tempore fugiat unde molestias ipsum repellendus, architecto autem nobis laudantium eligendi!
                Nesciunt
                illo similique delectus accusamus?</p>
            <p class="card-text"><small class="text-body-secondary"></small></p>
        </div>
<!-- hcards end -->
'''

ABOUT_US_DETAIL = '''
  <div class="row">
    <div class="col-sm-8 offset-sm-2">
      <h2>Vizyonumuz</h2>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa totam, earum ut itaque consectetur dolores, accusantium laudantium ipsam est cupiditate ipsa, officia neque deleniti ratione omnis corporis quo excepturi necessitatibus!</p>
      <p>Cumque adipisci alias rerum aspernatur molestias odio aperiam id. Est maiores iusto amet sapiente accusamus voluptatem expedita perspiciatis possimus eius ut laudantium aliquid quo tenetur iste maxime quidem, sunt odit.</p>
      <p>Magnam ipsum facere modi voluptates ab dolorem suscipit dicta a numquam eveniet reprehenderit eum odio, reiciendis neque et consequuntur cumque. Et quae dolorem necessitatibus totam laboriosam fugit vero, eveniet nam.</p>
      <hr />
      <h2>Misyonumuz</h2>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates unde autem nisi sed, porro in doloribus, consectetur magni ipsam veritatis magnam debitis nulla quos! Ab aperiam cupiditate incidunt corporis pariatur?</p>
      <p>Repellendus libero ex ab facilis, delectus eos in saepe doloremque impedit sequi, officiis omnis cumque. Delectus sequi nihil in. Nam sequi temporibus sapiente veritatis necessitatibus! Repudiandae, animi! Itaque, soluta alias.</p>
      <p>Porro, tempore? Minima magni dolorem expedita maxime non repellat nemo id quod nostrum sed, voluptate quibusdam quis aliquid exercitationem, nihil autem obcaecati similique molestias optio doloremque repudiandae. Cupiditate, expedita quod.</p>
      <p>Ea iusto ratione libero quis laboriosam pariatur mollitia similique, iure placeat ex maxime commodi quidem inventore reiciendis fugiat cumque dolor omnis quae ullam dolores nostrum adipisci quam soluta voluptates. Dolorum.</p>
      <ul>
        <li>Lorem, ipsum.</li>
        <li>Expedita, aliquid.</li>
        <li>Molestiae, minus!</li>
        <li>Autem, rerum.</li>
      </ul>
    </div>
  </div>
'''

CONTACT_DETAIL = '''
 <div class="row mb-5">
    <div class="col-sm-8 offset-sm-2">
      <h2>Adresimiz</h2>
      <address>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tenetur sequi atque quo quis eligendi temporibus, recusandae voluptatibus nihil amet provident!</p>
      </address>
      <hr />
      <h2 class="mt-5">Bizimle Elaqe Saxlayin</h2>
      <form class="row g-3">
        <div class="row g-3">
          <div class="col">
            <input type="text" class="form-control" placeholder="Ad" aria-label="Ad" />
          </div>
          <div class="col">
            <input type="text" class="form-control" placeholder="Soyad" aria-label="Soyad" />
          </div>
        </div>
        <div class="col-12">
          <label for="inputAddress" class="form-label">Seher/Rayon</label>
          <input type="text" class="form-control" id="inputAddress" />
        </div>
        <div class="col-12">
          <label for="inputEmail4" class="form-label">Email</label>
          <input type="email" class="form-control" id="inputEmail4" />
        </div>
        <div class="col-12">
          <label for="Aciqlama" class="form-label">Aciqlama</label>
          <textarea class="form-control" placeholder="Bura yazin..." id="floatingTextarea"></textarea>
        </div>
        <div class="col-12">
          <label for="inputState" class="form-label">Bizi Nece Tapdiniz?</label>
          <select id="inputState" class="form-select">
            <option selected>Secin...</option>
            <option>Sosial Shebeke</option>
            <option>Radio Reklami</option>
            <option>TV Reklami</option>
            <option>Facebook</option>
            <option>Twitter</option>
            <option>Instagram</option>
          </select>
        </div>

        <div class="col-12">
          <button type="submit" class="btn btn-primary">Gonder</button>
        </div>
      </form>
    </div> 
</div> 
'''

FAKE_DB_PAGES = [
    {"url": "elaqe", "detail": CONTACT_DETAIL, "title": "Elaqe"},
    {"url": "haqqimizda", "detail": ABOUT_US_DETAIL,"title": "Haqqimizda"},
    {"url": "vizyonumuz", "detail": VISION_DETAIL,"title": "Vizyonumuz"},
]
