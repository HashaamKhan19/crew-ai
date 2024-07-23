## Getting Started

### Prerequisites

- Python >=3.10
- Poetry

### Installation

1. Clone the repository

2. Install dependencies using Poetry:

   ```bash
   poetry install --no-root
   ```

3. Set up your environment variables:

   create `.env` file and update the variables (OPENAI_API_KEY, OPENAI_ORGANIZATION_ID, SERPER_API_KEY) inside with your own values.

4. Activate the Poetry shell to run the examples:

   ```bash
   poetry shell
   ```

5. Run the code examples:

   ```bash
    python main.py
   ```