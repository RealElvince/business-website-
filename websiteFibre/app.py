# useful libraries
import streamlit as st

# configure streamlit app
st.set_page_config(
    page_title="baba-jayden-fibre-waks",
    page_icon="seedling",
    layout="wide"
)

# font size for tabs
style_css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1rem;
    }
    
</style>
'''

st.markdown(style_css, unsafe_allow_html=True)


# Use Local CSS files
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/style.css")

# set the tab bar menu
Home, Gallery, Product, Services, AboutUs, Contact = st.tabs(
    [" 🏛️ Home ", " 📷 Gallery   ", " 📦 Products", " 🛠️ Services ", " 🛈 About us   ", " 📞Contact    "]
)

# Home tab content
with Home:
    st.subheader("Welcome to BABA JAYDEN FIBRE WAKS!")
    st.subheader("Hi, I am Deryk Omondi :wave: !,CEO at BABA JAYDEN FIBRE WAKS.")
    st.markdown(
        "<p>As a fiberglass worker, my passion lies in the artistry and precision of crafting durable and versatile materials. Working with fiberglass is more than just a job for me; it's a dynamic blend of skill, creativity, and technical expertise. I find immense joy in transforming raw materials into intricate, custom pieces that serve diverse purposes.</p>",
        unsafe_allow_html=True)
    st.markdown("[<h3>Learn more...</h3>](https://www.facebook.com/profile.php?id=100075627175175&mibextid=ZbWKwL)",
                unsafe_allow_html=True)
    st.markdown("---", unsafe_allow_html=True)

    with st.container():
        left_column, center_column, right_column = st.columns(3)
        with left_column:
            st.header("What we do")
            st.write(
                """
                On our workshop ,w do the following activities:
                - Resin mixing-responsible for accurately mix fibreglass ,resign and other materials to create composite material used for molding pots and vases.
                - Cutting fibreglass matting-preparing matting by cutting it to the required sizes for molding process.
                - Molding and casting-setting up molds for the desired shapes and sizes of pots and vases.
                - Applying layers of fibreglass matting to molds ensuring proper reinforcement and thickness.
                - Coating the fibreglass layers with resin to bind the fibers together.
                - Curing-Allowing the molded pieces to cure and harden,ensuring structural integrity.
                - Sanding and shaping-smoothing the surfaces and edges of vases ,enhancing their aesthetic appeal.
                - Color application-adding color to the fibreglass material or applying paints and finishes to achieve specific aesthetic effects as per customer requests.
                - Fixtures and Fittings-attaching additional elements such as bases,stands.
                - Packaging and shipping-Coordinating logistics and ensuring timely delivery of products to clients
                - Maintenance and clean-up -Regularly maintaining machinery and tools used in production process
                - Work area clean-up-keeping work area clean and organized for efficient and safe operations.
                """
            )
        with center_column:
            st.image("image1.png", caption="This is one of the vases we have designed.", width=390)
        with right_column:
            st.image('image2.png', caption="A red vase for house plant.", width=390)
    st.markdown("---", unsafe_allow_html=True)
    st.header("Message to our clients")
    st.write(
        "Our collection stands as a testament to the fusion of aesthetic appeal and durability. Each piece is a masterpiece, meticulously crafted to enhance both the visual allure of your space and the practicality that modern living demands. From sleek and contemporary designs to classic and timeless styles, our homepage presents a spectrum of options that cater to diverse tastes and preferences.")
    st.write(
        "The inherent versatility of fiberglass as a material allows us to push the boundaries of design, resulting in pots and vases that not only serve as striking focal points but also withstand the test of time. On our homepage, you'll find a showcase of these versatile creations, each telling a unique story of creativity and innovation.")
    st.write(
        "As you navigate through the various sections of our website, you'll encounter collections that cater to different aesthetics and interior design themes. Whether you're seeking a statement piece for a minimalist setting or an ornate vase to complement a more traditional decor, our homepage is your gateway to a curated selection that meets every design aspiration.")
    st.write(
        "We understand that your home is a reflection of your personality, and our website's homepage is designed to inspire and guide you in curating a space that truly feels like yours. Explore the intricate details, the thoughtful designs, and the quality that defines our fiberglass pots and vases.")
    st.write(
        "In the spirit of customer-centricity, our homepage not only serves as a visual feast but also provides a user-friendly experience. Effortlessly browse through categories, discover the latest additions, and find inspiration through featured collections. Each click opens a door to a world of possibilities, inviting you to reimagine your living spaces with our exceptional fiberglass creations.")
    st.write(
        "In summary, our website's homepage is more than just an introduction to our products; it's an invitation to explore, dream, and transform your surroundings. We invite you to embark on this aesthetic journey with us, where fiberglass artistry meets the canvas of your home.")
    st.markdown("---", unsafe_allow_html=True)

# Gallery content
with Gallery:
    st.write(
        "Welcome to our gallery page, where every image tells a story of craftsmanship and creativity. Immerse yourself in a visual feast showcasing our diverse collection of fiberglass pots and vases. Each page unfolds a tapestry of design, offering a glimpse into the artistry that defines our brand.")
    st.write(
        "In this curated space, witness the seamless blend of form and function. Explore the sleek lines of modern designs or get lost in the intricate details of timeless classics. Our gallery pages serve as a virtual exhibition, inviting you to appreciate the versatility of fiberglass as it takes shape in various styles and sizes.")
    st.write(
        "Dive into thematic collections that cater to different moods and aesthetics. From contemporary chic to rustic elegance, our gallery pages are a reflection of the thoughtfulness and innovation poured into each creation. Discover how our pots and vases can transform ordinary spaces into extraordinary showcases of sophistication.")
    st.write(
        "Whether you're an interior design enthusiast or a homeowner looking for that perfect accent piece, our gallery pages are your window into a world of possibilities. Imbued with the spirit of artistic exploration, each image is a testament to our commitment to quality and aesthetics.")
    st.write(
        "In the realm of fiberglass artistry, our gallery pages stand as a testament to the marriage of innovation and tradition. Take your time, savor the details, and let the visual journey guide you towards finding the perfect fiberglass pot or vase that resonates with your unique style. Welcome to a gallery experience that goes beyond the ordinary, where every page is a canvas waiting to be explored.")
    st.markdown("---", unsafe_allow_html=True)
    st.header("Our Aesthetic Pots and Vases")
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image("1.jpg", width=300)
            st.image("2.jpg", width=300)
            st.image("3.jpg", width=280)
            st.image("4.jpg", width=295)
        with col2:
            st.image("5.jpg", width=300)
            st.image("6.jpg", width=300)
            st.image("7.jpg", width=300)
            st.image("8.jpg", width=300)
            st.image("9.jpg", width=298)

        with col3:
            st.image("10.jpg", width=300)
            st.image("11.jpg", width=300)
            st.image("12.jpg", width=300)
            st.image("13.jpg", width=300)
            st.image("14.jpg", width=293)
        with col4:
            st.image("16.jpg", width=300)
            st.image("17.jpg", width=300)
            st.image("18.jpg", width=300)
            st.image("19.jpg", width=300)
            st.image("20.jpg", width=298)
        with col5:
            st.image("23.jpg", width=300)
            st.image("24.jpg", width=300)
            st.image("25.jpg", width=300)
            st.image("26.jpg", width=300)
            st.image("27.jpg", width=295)
    st.markdown("---", unsafe_allow_html=True)
    st.header("Workshop Images")
    st.write(
        'To our esteemed customers,we also repair water tanks  which involves reinforcing and sealing the tank with layers of fiberglass mat and resin.')
    column1, column2, column3 = st.columns(3)
    with column1:
        st.image("29.jpg", width=450)
        st.image("34.jpg", width=450)
    with column2:
        st.image("28.jpg", width=450)
        st.image("30.jpg", width=450)
    with column3:
        st.image("31.jpg", width=450)
        st.image("32.jpg", width=450)
    st.markdown("---", unsafe_allow_html=True)

# Product Content
with Product:
    st.write(
        "Explore a world of elegance with our premium line of fiberglass pots and vases. Our products stand at the intersection of aesthetic brilliance and durability, offering a curated collection that elevates your living spaces.")
    st.markdown("---", unsafe_allow_html=True)
    st.header("Key Features:")
    st.subheader("1.Durability Beyond Compare:")
    st.write(
        "Our fiberglass pots and vases are built to withstand the test of time. The use of high-quality fiberglass materials ensures exceptional durability, making these containers resistant to cracking, fading, and weathering. Enjoy long-lasting beauty in any environment, be it a sunny patio or a cozy indoor corner.")
    st.subheader("2.Lightweight Elegance:")
    st.write(
        "Despite their robust construction, these pots and vases remain surprisingly lightweight. Move and arrange your greenery effortlessly, whether you're redecorating your living room or revamping your garden. The lightweight design also makes them an excellent choice for balcony gardens and rooftop spaces.")
    st.subheader("3.Versatile Design:")
    st.write(
        "The sleek and contemporary design of our fiberglass pots and vases effortlessly complements any decor style. Whether you prefer a minimalist look, a classic aesthetic, or something more eclectic, these containers add a touch of sophistication to your space. Choose from various shapes and sizes to suit your unique taste.")
    st.subheader("4.Weather-Resistant Finish:")
    st.write(
        "Our fiberglass pots and vases feature a weather-resistant finish that protects them from the elements. Rain or shine, these containers maintain their visual appeal, making them an ideal choice for both indoor and outdoor use.")
    st.subheader("5.Easy Maintenance:")
    st.write(
        "Cleaning and maintaining your plant containers has never been easier. The smooth surface of fiberglass allows for quick and hassle-free cleaning, ensuring that your pots and vases always look their best. Spend more time enjoying your greenery and less time on upkeep.")
    st.subheader("6. Customization Options:")
    st.write(
        "Personalize your space with our customizable fiberglass pots and vases. Choose from a range of colors to match your decor or create a statement piece with bold hues. The customization options allow you to express your individual style and enhance the overall aesthetics of your surroundings.")
    st.markdown("---", unsafe_allow_html=True)

    st.subheader("Ideal for:")
    st.write(
        """
    
    - Home Gardens
    - Indoor Plants
    - Outdoor Landscaping
    - Commercial Spaces
    - Restaurants and Cafe
    - Events and Weddings

    Elevate your plant game with our fiberglass pots and vases. Experience the perfect fusion of style and functionality. Shop now and redefine the way you showcase your greenery!
    """
    )
    st.markdown("---", unsafe_allow_html=True)

# Service page contents
with Services:
    st.write(
        'Welcome to our comprehensive services for fiberglass pots and vases. At BABA JAYDEN FIBRE WAKS, we dont just offer exceptional products; we provide a range of services to ensure your experience is seamless from selection to installation.The following are our customer services:')
    st.markdown("---", unsafe_allow_html=True)
    st.subheader("1. Consultation Services:")
    st.write(
        "Our expert team is here to guide you through the selection process. Whether you're an individual looking to enhance your home or a business owner aiming to revamp a commercial space, our consultants offer personalized advice to help you choose the perfect fiberglass pots and vases that align with your vision and needs.")
    st.subheader("2. Custom Design Solutions:")
    st.write(
        "Make a statement with our custom design solutions. If you have a specific vision in mind, our design team can collaborate with you to create bespoke fiberglass pots and vases tailored to your unique requirements. From size and shape to color and finish, we bring your ideas to life.")
    st.subheader("3. Delivery and Installation:")
    st.write(
        "Leave the heavy lifting to us. Our delivery and installation services ensure that your fiberglass pots and vases are safely transported and professionally set up in your chosen space. Sit back and watch as your surroundings transform with minimal effort on your part.")
    st.subheader("4. Maintenance and Repairs:")
    st.write(
        "Our commitment to your satisfaction extends beyond the purchase. Benefit from our maintenance and repair services, designed to keep your fiberglass pots and vases in pristine condition. From minor touch-ups to comprehensive repairs, we ensure that your investment lasts for years to come.")
    st.subheader("5. Bulk Orders and Wholesale Pricing:")
    st.write(
        "For businesses, landscape designers, and event planners, we offer competitive bulk pricing and streamlined ordering processes. Enhance your projects with our fiberglass pots and vases, knowing that you're getting quality products at cost-effective rates.")
    st.subheader("6. Educational Workshops:")
    st.write(
        "Learn the best practices for caring and styling with fiberglass pots and vases through our educational workshops. These sessions provide insights into plant care, design principles, and the optimal use of fiberglass containers, empowering you to make the most of your investment.")
    st.subheader("7. Customer Support:")
    st.write(
        "Our customer support team is always ready to assist you. Whether you have questions about our products, need guidance on maintenance, or require help with an order, our friendly and knowledgeable team is just a phone call or email away.")
    st.write("##")
    st.write(
        "At BABA JAYDEN FIBRE WAKS, we believe in providing a holistic experience. Explore our services and discover how we can turn your vision into reality with our premium fiberglass pots and vases. Transform your spaces with elegance and ease—choose our pots and vases workshop for all your fiberglass container needs.")
    st.markdown("---", unsafe_allow_html=True)

# About us content page
with AboutUs:
    st.write(
        "Welcome to BABA JAYDEN FIBRE WAKS, where innovation, craftsmanship, and a passion for design converge to redefine the artistry of fiberglass. Our journey began with a vision to create products that seamlessly blend functionality with aesthetics, transforming ordinary spaces into extraordinary showcases of elegance.")
    st.markdown("---", unsafe_allow_html=True)
    st.subheader("Our Story:")
    st.write(
        "Established in 2017, BABA JAYDEN FIBRE WAKS was founded on the belief that interior and exterior spaces should be adorned with timeless pieces that reflect individual style. Our journey has been marked by a commitment to quality, a dedication to innovation, and an unwavering pursuit of excellence in fiberglass craftsmanship")
    st.markdown("---", unsafe_allow_html=True)
    st.subheader("Crafting Excellence:")
    st.write(
        "At the heart of our brand is a team of skilled artisans and designers who bring life to our vision. Each fiberglass pot and vase is meticulously crafted, blending traditional techniques with modern design sensibilities. The result is a collection that stands as a testament to the marriage of art and functionality.")
    st.markdown("---", unsafe_allow_html=True)
    st.subheader("Innovation in Fiberglass:")
    st.write(
        "We pride ourselves on pushing the boundaries of what fiberglass can achieve. This versatile material allows us to create lightweight, durable, and intricately detailed products that defy expectations. Our dedication to innovation is reflected in every piece, making our fibre-glass workshop a trailblazer in the world of fiberglass artistry.")
    st.markdown("---", unsafe_allow_html=True)
    st.subheader("Customer-Centric Approach:")
    st.write(
        "More than a brand, we are a partner in your design journey. Our customer-centric approach is woven into every aspect of BABA JAYDEN FIBRE WAKS. From personalized consultations to customization services, we strive to ensure that your experience with us is as exceptional as our products.")
    st.markdown("---", unsafe_allow_html=True)
    st.subheader("Sustainability Commitment:")
    st.write(
        "As stewards of the environment, we are committed to sustainable practices. Our manufacturing processes prioritize eco-friendly materials and responsible production methods. Choose [Your Brand Name] not only for the beauty it brings to your spaces but also for the conscientious approach we take towards our planet.")
    st.markdown("---", unsafe_allow_html=True)
    st.subheader("Join Us on the Journey:")
    st.write(
        "Whether you're an interior design enthusiast, a homeowner, or a landscaping professional, [Your Brand Name] invites you to join us on a journey of artistic exploration. Discover the beauty of fiberglass, explore our curated collections, and let us be a part of enhancing the aesthetic tapestry of your surroundings.")

    st.write("")
    st.write(
        "Thank you for choosing BABA JAYDEN FIBRE WAKS. We look forward to being a part of your design narrative, where every piece tells a story of craftsmanship, innovation, and enduring beauty.")
    st.markdown("---", unsafe_allow_html=True)

# Contact Page
with Contact:
    st.write(
        "We value your connection and ready to assist you. Feel free to reach out to us through the following channels:")
    st.markdown("---", unsafe_allow_html=True)
    st.subheader("Customer Support:")
    st.write(
        "For inquiries about our products, customization options, or assistance with your order, our dedicated customer support team is ready to help.")
    st.write(":envelope: derykadu@gmail.com")
    st.write(":telephone: +254721289920")
    st.markdown("---", unsafe_allow_html=True)
    st.subheader("Visit Our Workshop:")
    st.write(
        "Immerse yourself in the world of [Your Brand Name] by visiting our workshop. Experience the craftsmanship of our fiberglass pots and vases firsthand.")
    st.write(" Address:📍Eldama Ravine ,Baringo County.")
    st.write("Business Hours: 🕖 MON-SAT 8:00 am to 7:30 pm. ")
    st.markdown("---", unsafe_allow_html=True)
    st.subheader("Connect on Social Media:")
    st.write("Stay updated on the latest designs, promotions, and news by following us on social media.")
    st.write("ⓕ - Baba Jayden FIbre Waks(Facebook page)")
    st.write("𝕏 - Baba Jayden Fibre Waks")
    st.markdown("---", unsafe_allow_html=True)
    st.subheader("Feedback and Suggestions:")
    st.write("We value your input! Share your feedback and suggestions to help us improve.")
    st.write(":envelope: derykadu@gmail.com")
    st.markdown("---", unsafe_allow_html=True)

    # Get in touch with us
    with st.container():
        st.header("Get In Touch With Us!")

        # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/c" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="text" name="phone" placeholder="Your phone number" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
