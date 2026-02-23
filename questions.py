"""
WebDev Quiz — Full Question Bank
Covers: HTML, CSS, JavaScript, React, Node.js, Express, Java, C#, .NET
"""

TOPICS_META = [
    {'id': 'html',    'name': 'HTML',       'emoji': '🌐', 'color': '#e44d26', 'bg': '#fff4f0'},
    {'id': 'css',     'name': 'CSS',        'emoji': '🎨', 'color': '#264de4', 'bg': '#f0f3ff'},
    {'id': 'js',      'name': 'JavaScript', 'emoji': '⚡', 'color': '#e6c000', 'bg': '#fffbeb'},
    {'id': 'react',   'name': 'React',      'emoji': '⚛',  'color': '#00b4d8', 'bg': '#f0faff'},
    {'id': 'node',    'name': 'Node.js',    'emoji': '🟢', 'color': '#3d9142', 'bg': '#f0fdf4'},
    {'id': 'express', 'name': 'Express',    'emoji': '🚀', 'color': '#404040', 'bg': '#f5f5f5'},
    {'id': 'java',    'name': 'Java',       'emoji': '☕', 'color': '#f89820', 'bg': '#fff8ed'},
    {'id': 'csharp',  'name': 'C#',         'emoji': '🔷', 'color': '#9b4ff8', 'bg': '#faf0ff'},
    {'id': 'dotnet',  'name': '.NET',       'emoji': '🟣', 'color': '#512bd4', 'bg': '#f0eeff'},
]

QUESTIONS = {
    'html': [
        {'diff': 'easy', 'q': 'What does HTML stand for?',
         'opts': ['HyperText Markup Language', 'High-Tech Modern Language', 'HyperText Machine Learning', 'Home Tool Markup Language'],
         'ans': 0, 'exp': 'HTML stands for HyperText Markup Language — the standard language for creating web pages.'},

        {'diff': 'easy', 'q': 'Which tag creates a hyperlink?',
         'opts': ['<link>', '<href>', '<a>', '<url>'],
         'ans': 2, 'exp': 'The <a> (anchor) tag creates hyperlinks. The href attribute specifies the destination URL.'},

        {'diff': 'easy', 'q': 'Which HTML tag defines the document title shown in the browser tab?',
         'opts': ['<meta>', '<head>', '<title>', '<header>'],
         'ans': 2, 'exp': 'The <title> element sets the browser tab text and must be placed inside the <head> element.'},

        {'diff': 'easy', 'q': 'Which tag is used to display an image?',
         'opts': ['<picture>', '<img>', '<image>', '<src>'],
         'ans': 1, 'exp': '<img> is the self-closing tag for images. The src attribute sets the image URL and alt provides alternative text.'},

        {'diff': 'easy', 'q': 'Which attribute adds a tooltip to an HTML element?',
         'opts': ['tooltip', 'hint', 'title', 'alt'],
         'ans': 2, 'exp': 'The title attribute creates a tooltip that appears when hovering over most HTML elements.'},

        {'diff': 'easy', 'q': 'What tag makes text appear in bold AND conveys importance?',
         'opts': ['<b>', '<bold>', '<strong>', '<em>'],
         'ans': 2, 'exp': '<strong> makes text bold AND adds semantic importance for screen readers. <b> is just visual styling.'},

        {'diff': 'easy', 'q': 'Which HTML element creates an unordered (bulleted) list?',
         'opts': ['<ol>', '<li>', '<ul>', '<list>'],
         'ans': 2, 'exp': '<ul> creates an unordered list with bullets. <ol> creates an ordered (numbered) list. <li> is the list item.'},

        {'diff': 'hard', 'q': 'What does the defer attribute do on a <script> tag?',
         'opts': ['Loads script asynchronously, may run before DOM ready', 'Delays execution until HTML is fully parsed', 'Skips script on slow connections', 'Compresses the script file'],
         'ans': 1, 'exp': 'defer loads the script in the background and executes it only after the entire HTML document has been parsed.'},

        {'diff': 'hard', 'q': 'What is the purpose of the <datalist> element?',
         'opts': ['Creates a dropdown select menu', 'Provides autocomplete suggestions for <input>', 'Stores hidden form data', 'Lists all CSS variables'],
         'ans': 1, 'exp': '<datalist> provides a list of predefined autocomplete options for an <input> element via the list attribute.'},

        {'diff': 'hard', 'q': 'What is the correct use of the <figure> element?',
         'opts': ['For CSS background images only', 'Self-contained media like images with optional <figcaption>', 'A navigation container', 'A geometric shape element'],
         'ans': 1, 'exp': '<figure> wraps self-contained content like images, diagrams, or code snippets with an optional <figcaption>.'},
    ],

    'css': [
        {'diff': 'easy', 'q': 'What does CSS stand for?',
         'opts': ['Computer Style Sheets', 'Creative Style Sheets', 'Cascading Style Sheets', 'Colorful Style Sheets'],
         'ans': 2, 'exp': 'CSS stands for Cascading Style Sheets. "Cascading" refers to how styles are applied based on specificity and order.'},

        {'diff': 'easy', 'q': 'Which property changes the text color?',
         'opts': ['font-color', 'text-color', 'color', 'foreground'],
         'ans': 2, 'exp': 'The color property sets the foreground (text) color. It accepts color names, hex, rgb, hsl values.'},

        {'diff': 'easy', 'q': 'Which property sets the background color?',
         'opts': ['bgcolor', 'background-color', 'bg', 'bg-color'],
         'ans': 1, 'exp': 'background-color sets the background color of an element. You can also use the shorthand background property.'},

        {'diff': 'easy', 'q': 'How do you add a comment in CSS?',
         'opts': ['// comment', '<!-- comment -->', '/* comment */', '# comment'],
         'ans': 2, 'exp': 'CSS comments use /* */ syntax and can span multiple lines. They are completely ignored by the browser.'},

        {'diff': 'easy', 'q': 'Which CSS property controls the font size?',
         'opts': ['text-size', 'font-style', 'font-size', 'text-style'],
         'ans': 2, 'exp': 'font-size controls text size. Common units: px (pixels), em (relative to parent), rem (relative to root), % (percentage).'},

        {'diff': 'easy', 'q': 'How do you select an element with id="header" in CSS?',
         'opts': ['.header', '#header', 'header', '*header'],
         'ans': 1, 'exp': '# selects by ID. IDs are unique per page. . selects by class. IDs have higher specificity than classes.'},

        {'diff': 'hard', 'q': 'What does "display: flex" do to an element?',
         'opts': ['Makes the element invisible', 'Creates a CSS Grid layout', 'Makes the element a flex container', 'Removes all padding and margin'],
         'ans': 2, 'exp': 'display: flex turns the element into a flex container. Its direct children become flex items, enabling Flexbox layout.'},

        {'diff': 'hard', 'q': 'What is the CSS Box Model from inside to outside?',
         'opts': ['Content → Padding → Border → Margin', 'Margin → Border → Padding → Content', 'Content → Border → Padding → Margin', 'Padding → Content → Margin → Border'],
         'ans': 0, 'exp': 'Box Model order: Content (innermost) → Padding → Border → Margin (outermost). box-sizing: border-box includes padding+border in width.'},

        {'diff': 'hard', 'q': 'Which CSS selector has the highest specificity?',
         'opts': ['Element selector (p)', 'Class selector (.box)', 'ID selector (#main)', 'Inline style attribute'],
         'ans': 3, 'exp': 'Specificity order: inline styles > ID > class/attribute/pseudo-class > element/pseudo-element. !important overrides all.'},

        {'diff': 'hard', 'q': 'What does "position: absolute" do?',
         'opts': ['Fixes element to viewport', 'Positions relative to nearest positioned ancestor', 'Removes element from flow, positions to viewport', 'Stacks elements on top of each other'],
         'ans': 1, 'exp': 'position: absolute removes the element from the normal flow and positions it relative to its nearest positioned (non-static) ancestor.'},
    ],

    'js': [
        {'diff': 'easy', 'q': 'How do you declare a constant variable in JavaScript?',
         'opts': ['var', 'let', 'const', 'static'],
         'ans': 2, 'exp': 'const declares a variable with a constant binding. You cannot reassign it, but objects/arrays declared with const can still be mutated.'},

        {'diff': 'easy', 'q': 'What does console.log() do?',
         'opts': ['Creates a log file', 'Shows a popup alert', 'Prints output to the browser console', 'Sends data to the server'],
         'ans': 2, 'exp': 'console.log() prints messages to the browser developer console. Essential for debugging during development.'},

        {'diff': 'easy', 'q': 'Which of these is NOT a JavaScript data type?',
         'opts': ['String', 'Boolean', 'Float', 'Undefined'],
         'ans': 2, 'exp': 'Float is not a JS type. JavaScript uses a single "Number" type for all numeric values — both integers and floating point numbers.'},

        {'diff': 'easy', 'q': 'How do you write a single-line comment in JavaScript?',
         'opts': ['<!-- comment -->', '/* comment */', '// comment', '## comment'],
         'ans': 2, 'exp': 'Single-line comments in JavaScript start with //. Multi-line comments use /* */ just like CSS.'},

        {'diff': 'easy', 'q': 'Which method adds an element to the END of an array?',
         'opts': ['push()', 'pop()', 'shift()', 'unshift()'],
         'ans': 0, 'exp': 'push() adds one or more elements to the END of an array and returns the new length. pop() removes the last element.'},

        {'diff': 'hard', 'q': 'What does typeof null return in JavaScript?',
         'code': 'console.log(typeof null);',
         'opts': ['"null"', '"undefined"', '"object"', '"boolean"'],
         'ans': 2, 'exp': 'typeof null returns "object" — this is a famous JavaScript bug from 1995 that was never fixed for backwards compatibility.'},

        {'diff': 'hard', 'q': 'What does the spread operator do?',
         'code': 'const arr = [1, 2, 3];\nconst copy = [...arr, 4, 5];',
         'opts': ['Creates a reference to arr', 'Spreads elements into a new array/object', 'Deletes elements from arr', 'Sorts the array'],
         'ans': 1, 'exp': 'The spread operator (...) expands iterable elements. Great for copying arrays/objects or merging them without mutation.'},

        {'diff': 'hard', 'q': 'What is a Promise in JavaScript?',
         'opts': ['A loop that never ends', 'An object representing eventual completion of an async operation', 'A type of variable declaration', 'A way to import modules'],
         'ans': 1, 'exp': 'A Promise is an object representing a value available now, in the future, or never. Used for async operations like API calls.'},

        {'diff': 'hard', 'q': 'What is event bubbling?',
         'opts': ['An event that fires only once', 'Events propagating from child up to parent elements', 'A memory leak from events', 'An error in the event loop'],
         'ans': 1, 'exp': 'Event bubbling means when an event fires on an element, it also triggers on all ancestor elements going up to the document root.'},

        {'diff': 'hard', 'q': 'What is the difference between == and === in JavaScript?',
         'opts': ['No difference', '=== is faster than ==', '== checks value only, === checks value AND type', '=== only works for numbers'],
         'ans': 2, 'exp': '== does type coercion (0 == "0" is true). === is strict equality — checks both value AND type (0 === "0" is false). Always prefer ===.'},
    ],

    'react': [
        {'diff': 'easy', 'q': 'What is JSX in React?',
         'opts': ['A JavaScript file extension', 'Syntax that lets you write HTML-like code in JavaScript', 'A React testing library', 'A state management tool'],
         'ans': 1, 'exp': 'JSX is a syntax extension for JavaScript that looks like HTML. React uses Babel to transform it into regular JavaScript function calls.'},

        {'diff': 'easy', 'q': 'Which Hook manages state in a function component?',
         'opts': ['useEffect', 'useContext', 'useState', 'useRef'],
         'ans': 2, 'exp': 'useState is the primary React Hook for adding state to function components. It returns [currentValue, setterFunction].'},

        {'diff': 'easy', 'q': 'What is a React component?',
         'opts': ['A CSS class', 'A reusable piece of UI that returns JSX', 'A database query', 'A type of HTTP request'],
         'ans': 1, 'exp': 'A React component is a reusable, self-contained UI building block. It can be a function or class that returns JSX.'},

        {'diff': 'easy', 'q': 'How do you pass data to a child component in React?',
         'opts': ['Using global variables', 'Using props', 'Using localStorage', 'Using the DOM directly'],
         'ans': 1, 'exp': 'Props (properties) are how data flows from parent to child components in React. They are read-only inside the child.'},

        {'diff': 'hard', 'q': 'When does useEffect run with an empty array []?',
         'opts': ['On every render', 'Never runs', 'Only once after the first render', 'Only when state changes'],
         'ans': 2, 'exp': 'useEffect with [] dependency array runs only once — after the initial render. Equivalent to componentDidMount in class components.'},

        {'diff': 'hard', 'q': 'What is the Virtual DOM?',
         'opts': ['A DOM stored in a database', 'A lightweight in-memory copy of the real DOM React uses for efficient updates', 'A DOM for virtual machines', 'A deprecated React feature'],
         'ans': 1, 'exp': 'React keeps a Virtual DOM in memory. When state changes, it diffs the new virtual DOM with the old one and only updates what changed in the real DOM.'},

        {'diff': 'hard', 'q': 'What does the key prop do in React lists?',
         'code': 'items.map(item => <li key={item.id}>{item.name}</li>)',
         'opts': ['Adds CSS styling', 'Encrypts list data', 'Helps React identify which items changed for efficient re-rendering', 'Sets the tab order'],
         'ans': 2, 'exp': 'The key prop gives React a stable identity for each list item so it can efficiently update, add, or remove items without re-rendering everything.'},

        {'diff': 'hard', 'q': 'What does useReducer do?',
         'opts': ['Reduces the size of components', 'An alternative to useState for complex state logic', 'Removes unused state', 'Combines multiple components'],
         'ans': 1, 'exp': 'useReducer manages complex state logic using a reducer function (state, action) => newState. Good when next state depends on previous state.'},
    ],

    'node': [
        {'diff': 'easy', 'q': 'What is Node.js?',
         'opts': ['A browser plugin', 'A JavaScript runtime built on Chrome V8 engine', 'A CSS framework', 'A database system'],
         'ans': 1, 'exp': 'Node.js is a JavaScript runtime that lets you run JavaScript on the server — outside the browser — using Chrome\'s V8 engine.'},

        {'diff': 'easy', 'q': 'Which command installs a package with npm?',
         'opts': ['npm get', 'npm download', 'npm install', 'npm add'],
         'ans': 2, 'exp': 'npm install <package> (or npm i) installs a package from the npm registry and adds it to node_modules.'},

        {'diff': 'easy', 'q': 'How do you import a module in Node.js (CommonJS)?',
         'opts': ['import module from "m"', 'require("module")', 'include("module")', 'using module'],
         'ans': 1, 'exp': 'In CommonJS (the default in Node.js), require() imports modules. Modern Node.js also supports ES module syntax (import/export).'},

        {'diff': 'easy', 'q': 'Which command creates a package.json for a new project?',
         'opts': ['node start', 'npm create', 'npm init', 'node new'],
         'ans': 2, 'exp': 'npm init creates a package.json file. Use npm init -y to skip the questions and accept all defaults.'},

        {'diff': 'hard', 'q': 'What is the event loop in Node.js?',
         'opts': ['A for loop built into Node', 'A mechanism that handles async callbacks without blocking the main thread', 'A logging system', 'A database connection pool'],
         'ans': 1, 'exp': 'The event loop allows Node.js to perform non-blocking I/O by offloading operations to the system kernel and running callbacks when complete.'},

        {'diff': 'hard', 'q': 'What does process.env do?',
         'opts': ['Runs environment setup scripts', 'Provides access to environment variables', 'Monitors CPU usage', 'Lists all running Node processes'],
         'ans': 1, 'exp': 'process.env is an object containing the user\'s environment variables. Used to store config like DB connection strings, API keys, and ports.'},

        {'diff': 'hard', 'q': 'What is the purpose of package-lock.json?',
         'opts': ['Locks the Node.js version', 'Prevents editing package.json', 'Locks exact dependency versions for consistent installs', 'Encrypts your packages'],
         'ans': 2, 'exp': 'package-lock.json records the exact version of every installed package and its dependencies, ensuring consistent installs across environments.'},
    ],

    'express': [
        {'diff': 'easy', 'q': 'What is Express.js?',
         'opts': ['A database driver', 'A minimal, flexible Node.js web application framework', 'A CSS preprocessor', 'A testing library'],
         'ans': 1, 'exp': 'Express.js is a minimal, fast, unopinionated web framework for Node.js. Great for building REST APIs and web applications.'},

        {'diff': 'easy', 'q': 'Which method handles a GET request in Express?',
         'code': 'app.___("/home", (req, res) => res.send("Hello"));',
         'opts': ['app.post()', 'app.get()', 'app.fetch()', 'app.request()'],
         'ans': 1, 'exp': 'app.get() registers a route handler for HTTP GET requests. Express has similar methods: post(), put(), delete(), patch().'},

        {'diff': 'easy', 'q': 'What does res.json() do in Express?',
         'opts': ['Reads a JSON file from disk', 'Validates incoming JSON', 'Sends a JSON response to the client', 'Converts JSON to XML'],
         'ans': 2, 'exp': 'res.json() sends a JSON-formatted HTTP response and automatically sets Content-Type to application/json.'},

        {'diff': 'easy', 'q': 'How do you get a URL parameter in Express?',
         'code': 'app.get("/users/:id", (req, res) => { /* get id here */ });',
         'opts': ['req.query.id', 'req.params.id', 'req.body.id', 'req.url.id'],
         'ans': 1, 'exp': 'req.params.id accesses URL path parameters defined with :id. req.query is for ?key=value query strings. req.body is for POST body data.'},

        {'diff': 'hard', 'q': 'What is middleware in Express?',
         'opts': ['A database query layer', 'Functions that access req, res, and next in the request-response cycle', 'A frontend templating engine', 'A caching mechanism'],
         'ans': 1, 'exp': 'Middleware functions execute during the request/response cycle. They can modify req/res objects, end the cycle, or call next() to continue.'},

        {'diff': 'hard', 'q': 'What does the next() function do in Express middleware?',
         'opts': ['Sends the final response', 'Terminates the request permanently', 'Passes control to the next middleware function in the stack', 'Goes to the next line of code'],
         'ans': 2, 'exp': 'next() passes control to the next middleware. If not called and response not sent, the request will hang indefinitely.'},

        {'diff': 'hard', 'q': 'What is the purpose of express.Router()?',
         'opts': ['Handles URL redirects', 'Creates a mini application to organize routes into separate files', 'Manages WebSocket connections', 'Monitors route performance'],
         'ans': 1, 'exp': 'express.Router() creates a modular, mountable route handler — a "mini app" that lets you organize routes into separate files for cleaner code.'},
    ],

    'java': [
        {'diff': 'easy', 'q': 'Which keyword creates a new object instance in Java?',
         'opts': ['create', 'object', 'new', 'make'],
         'ans': 2, 'exp': 'The new keyword allocates memory and creates a new object instance, invoking the class constructor.'},

        {'diff': 'easy', 'q': 'What is the correct way to print to the console in Java?',
         'opts': ['console.log()', 'print()', 'System.out.println()', 'echo()'],
         'ans': 2, 'exp': 'System.out.println() prints a line to standard output. System.out.print() does the same without a newline character.'},

        {'diff': 'easy', 'q': 'Which data type stores a single character in Java?',
         'opts': ['String', 'char', 'letter', 'character'],
         'ans': 1, 'exp': 'char stores a single character like \'A\' using single quotes. String stores a sequence of characters using double quotes.'},

        {'diff': 'easy', 'q': 'What is the entry point of every Java application?',
         'opts': ['start()', 'run()', 'main()', 'init()'],
         'ans': 2, 'exp': 'Every Java application starts with the main() method: public static void main(String[] args). The JVM calls this to begin execution.'},

        {'diff': 'hard', 'q': 'What is the difference between == and .equals() for Strings in Java?',
         'opts': ['They are identical', '== compares references, .equals() compares content', '== compares content, .equals() compares references', '== is faster, equals() is more accurate'],
         'ans': 1, 'exp': '== checks if two String variables point to the same object in memory. .equals() compares the actual character content. Always use .equals() for Strings!'},

        {'diff': 'hard', 'q': 'What is a Java interface?',
         'opts': ['A GUI component', 'A contract defining methods a class must implement', 'A type of for loop', 'A data storage class'],
         'ans': 1, 'exp': 'An interface defines a contract of methods that implementing classes must provide. Used for abstraction and achieving multiple inheritance in Java.'},

        {'diff': 'hard', 'q': 'What does the static keyword mean in Java?',
         'opts': ['The variable cannot change', 'The member belongs to the class, not individual instances', 'The method runs at startup', 'The class cannot be extended'],
         'ans': 1, 'exp': 'static means the field/method belongs to the class itself, not to any specific object instance. Accessed via ClassName.member without creating an object.'},
    ],

    'csharp': [
        {'diff': 'easy', 'q': 'What is C# primarily used for?',
         'opts': ['Styling web pages', 'Database queries only', 'Building applications on the Microsoft/.NET platform', 'Low-level hardware programming'],
         'ans': 2, 'exp': 'C# is a modern, strongly-typed OOP language by Microsoft, used for web apps (ASP.NET), desktop, games (Unity), and cloud applications.'},

        {'diff': 'easy', 'q': 'Which keyword declares a class in C#?',
         'opts': ['def', 'function', 'class', 'type'],
         'ans': 2, 'exp': 'class declares a reference type in C#. For value types, use struct. Both can have fields, properties, methods, and constructors.'},

        {'diff': 'easy', 'q': 'What does var do in C#?',
         'opts': ['Declares a global variable', 'Declares a variable with implicit type inference', 'Creates a variable that can change type', 'Creates a nullable variable'],
         'ans': 1, 'exp': 'var in C# allows the compiler to infer the type from the assigned value. The type is still statically determined at compile time — not dynamic.'},

        {'diff': 'easy', 'q': 'What symbol is used for string interpolation in C#?',
         'code': 'string msg = $"Hello, {name}!";',
         'opts': ['@', '#', '$', '&'],
         'ans': 2, 'exp': 'The $ prefix enables string interpolation in C#. Variables and expressions in {curly braces} are evaluated and embedded in the string.'},

        {'diff': 'hard', 'q': 'What is a C# property?',
         'opts': ['A CSS-like attribute', 'A special getter/setter pair that encapsulates field access', 'A type of constructor', 'A read-only constant'],
         'ans': 1, 'exp': 'A C# property provides controlled access to a private field via get and set accessors. Enables encapsulation while appearing like a field to callers.'},

        {'diff': 'hard', 'q': 'What does async/await do in C#?',
         'code': 'public async Task<string> GetDataAsync() {\n  var result = await client.GetAsync(url);\n  return await result.Content.ReadAsStringAsync();\n}',
         'opts': ['Runs code in a background thread', 'Enables non-blocking async code that reads like synchronous code', 'Speeds up CPU-bound work', 'Creates multiple parallel threads'],
         'ans': 1, 'exp': 'async/await lets you write asynchronous, non-blocking code that looks and reads like simple synchronous code, without manual callback chaining.'},

        {'diff': 'hard', 'q': 'What is the difference between List<T> and Array in C#?',
         'opts': ['No difference', 'List<T> is dynamic size; Array is fixed size', 'Array is faster in all cases', 'List<T> can only store strings'],
         'ans': 1, 'exp': 'Array has a fixed size set at creation. List<T> is a dynamic collection that can grow or shrink. List<T> provides more methods like Add(), Remove(), Contains().'},
    ],

    'dotnet': [
        {'diff': 'easy', 'q': 'What is .NET?',
         'opts': ['A web browser', 'A programming language', 'A Microsoft framework for building cross-platform applications', 'A database engine'],
         'ans': 2, 'exp': '.NET is a free, open-source, cross-platform framework by Microsoft for building web, desktop, mobile, cloud, and IoT applications.'},

        {'diff': 'easy', 'q': 'What is NuGet in .NET?',
         'opts': ['A performance profiler', 'The package manager for .NET libraries', 'A unit testing framework', 'A code style formatter'],
         'ans': 1, 'exp': 'NuGet is the package manager for .NET, similar to npm for Node.js. Install packages with: dotnet add package PackageName.'},

        {'diff': 'easy', 'q': 'Which command runs a .NET application?',
         'opts': ['dotnet start', 'dotnet launch', 'dotnet run', 'dotnet execute'],
         'ans': 2, 'exp': 'dotnet run builds and runs your .NET application. dotnet build just compiles it. dotnet publish prepares it for deployment.'},

        {'diff': 'hard', 'q': 'What is ASP.NET Core?',
         'opts': ['A JavaScript framework', 'A cross-platform framework for building web apps and REST APIs with C#', 'A desktop GUI framework', 'A database ORM'],
         'ans': 1, 'exp': 'ASP.NET Core is a cross-platform, high-performance web framework for building modern web apps, REST APIs, and microservices using C#.'},

        {'diff': 'hard', 'q': 'What is Dependency Injection (DI) in .NET?',
         'opts': ['Installing NuGet packages', 'A technique where objects receive their dependencies externally instead of creating them', 'Injecting SQL into queries', 'A security vulnerability'],
         'ans': 1, 'exp': 'DI is a design pattern where a class receives dependencies from outside (injected) rather than creating them. Promotes loose coupling, testability, and the Single Responsibility Principle.'},

        {'diff': 'hard', 'q': 'What is Entity Framework Core?',
         'opts': ['A UI component library', 'An ORM that lets you work with databases using C# objects instead of SQL', 'A testing framework', 'A logging library'],
         'ans': 1, 'exp': 'EF Core is an Object-Relational Mapper (ORM) for .NET. It lets you query and save data using C# objects, generating SQL automatically.'},
    ],
}


def get_questions_by_topics(topic_ids: list, difficulty: str, count: int) -> list:
    """
    Return a shuffled list of questions for given topics and difficulty.
    If not enough questions match difficulty, falls back to all difficulties.
    """
    import random

    pool = []
    for tid in topic_ids:
        if tid not in QUESTIONS:
            continue
        qs = QUESTIONS[tid]
        if difficulty != 'mixed':
            filtered = [q for q in qs if q['diff'] == difficulty]
            qs = filtered if filtered else qs  # fallback to all if none match
        for q in qs:
            pool.append({**q, 'topic_id': tid})

    random.shuffle(pool)
    return pool[:count]


def get_topics_meta() -> list:
    return TOPICS_META
